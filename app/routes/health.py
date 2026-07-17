import io
from flask import Blueprint, render_template, request, redirect, url_for, flash, Response
from datetime import date
from app import db
from app.models.health import HealthRecord, HealthPlanItem

health_bp = Blueprint('health', __name__)


@health_bp.route('/')
def view():
    latest = HealthRecord.query.order_by(HealthRecord.date.desc()).first()
    records = HealthRecord.query.order_by(HealthRecord.date.desc()).all()
    plan_items = HealthPlanItem.query.order_by(HealthPlanItem.created_at.desc()).all()

    chart_data = []
    for r in reversed(records):
        if r.weight:
            chart_data.append({'date': r.date.strftime('%b %d') if r.date else '', 'weight': r.weight})

    return render_template('health.html',
        active_page='health',
        latest=latest,
        records=records,
        plan_items=plan_items,
        chart_data=chart_data,
    )


@health_bp.route('/add', methods=['POST'])
def add_record():
    weight = request.form.get('weight', type=float)
    height = request.form.get('height', type=float)
    age = request.form.get('age', type=int)
    gender = request.form.get('gender', '')
    body_fat = request.form.get('body_fat', type=float)
    record_date_str = request.form.get('date', '')

    record_date = date.fromisoformat(record_date_str) if record_date_str else date.today()
    record = HealthRecord(date=record_date, weight=weight, height=height, age=age, gender=gender, body_fat=body_fat)
    record.calculate_bmi()
    db.session.add(record)
    db.session.commit()
    flash('Health record added!', 'success')
    return redirect(url_for('health.view'))


@health_bp.route('/plan/<int:id>/complete', methods=['POST'])
def complete_plan_item(id):
    item = HealthPlanItem.query.get_or_404(id)
    item.completed = not item.completed
    db.session.commit()
    return redirect(url_for('health.view'))


@health_bp.route('/plan/<int:id>/delete', methods=['POST'])
def delete_plan_item(id):
    item = HealthPlanItem.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Plan item deleted.', 'info')
    return redirect(url_for('health.view'))


@health_bp.route('/export')
def export_data():
    records = HealthRecord.query.order_by(HealthRecord.date.desc()).all()
    latest = HealthRecord.query.order_by(HealthRecord.date.desc()).first()

    content = "Health Data Export\n"
    content += "=" * 40 + "\n\n"
    if latest:
        content += f"Current Profile:\n"
        content += f"  Weight: {latest.weight} kg\n"
        content += f"  Height: {latest.height} cm\n"
        content += f"  BMI: {latest.bmi}\n"
        content += f"  Body Fat: {latest.body_fat}%\n\n"

    content += "Records:\n"
    content += "-" * 40 + "\n"
    for r in records:
        content += f"\nDate: {r.date}\n"
        content += f"  Weight: {r.weight} kg\n"
        content += f"  Height: {r.height} cm\n"
        content += f"  BMI: {r.bmi}\n"
        content += f"  Body Fat: {r.body_fat}%\n"

    return Response(
        content,
        mimetype='text/plain',
        headers={'Content-Disposition': 'attachment; filename=health_data.txt'}
    )
