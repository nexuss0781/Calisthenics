import json
from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import date
from app import db
from app.models.plan import Plan

plan_bp = Blueprint('plan', __name__)


@plan_bp.route('/')
def view():
    plans = Plan.query.order_by(Plan.start_date.asc()).all()
    total_plans = Plan.query.count()
    completed_count = Plan.query.filter_by(status='completed').count()
    pending_count = Plan.query.filter_by(status='upcoming').count()
    progress_percent = round(completed_count / total_plans * 100) if total_plans > 0 else 0

    timeline_data = []
    for p in plans:
        timeline_data.append({
            'title': p.title,
            'type': p.plan_type,
            'start': p.start_date.isoformat() if p.start_date else '',
            'end': p.end_date.isoformat() if p.end_date else '',
            'status': p.status,
            'progress': p.progress_percent,
        })

    return render_template('plan.html',
        active_page='plan',
        plans=plans,
        total_plans=total_plans,
        completed_count=completed_count,
        pending_count=pending_count,
        progress_percent=progress_percent,
        timeline_data=json.dumps(timeline_data),
    )


@plan_bp.route('/add', methods=['POST'])
def add_plan():
    title = request.form.get('title', '').strip()
    plan_type = request.form.get('type', 'strength')
    start_date_str = request.form.get('start_date', '')
    end_date_str = request.form.get('end_date', '')
    description = request.form.get('description', '')
    if not title:
        flash('Plan title is required.', 'error')
        return redirect(url_for('plan.view'))
    start_date = date.fromisoformat(start_date_str) if start_date_str else None
    end_date = date.fromisoformat(end_date_str) if end_date_str else None
    plan = Plan(title=title, plan_type=plan_type, start_date=start_date,
                end_date=end_date, description=description)
    db.session.add(plan)
    db.session.commit()
    flash('Plan added!', 'success')
    return redirect(url_for('plan.view'))


@plan_bp.route('/<int:id>/delete', methods=['POST'])
def delete_plan(id):
    plan = Plan.query.get_or_404(id)
    db.session.delete(plan)
    db.session.commit()
    flash('Plan deleted.', 'info')
    return redirect(url_for('plan.view'))
