from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import date
from app import db
from app.models.goal import Goal

goals_bp = Blueprint('goals', __name__)


@goals_bp.route('/')
def view():
    goals = Goal.query.order_by(Goal.created_at.desc()).all()
    completed_count = Goal.query.filter_by(status='completed').count()
    total_goals = Goal.query.count()
    completion_percent = round(completed_count / total_goals * 100) if total_goals > 0 else 0
    return render_template('goals.html',
        active_page='goals',
        goals=goals,
        completed_count=completed_count,
        total_goals=total_goals,
        completion_percent=completion_percent,
    )


@goals_bp.route('/add', methods=['POST'])
def add_goal():
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '')
    target_date_str = request.form.get('target_date', '')
    if not title:
        flash('Goal title is required.', 'error')
        return redirect(url_for('goals.view'))
    target_date = date.fromisoformat(target_date_str) if target_date_str else None
    goal = Goal(title=title, description=description, target_date=target_date)
    db.session.add(goal)
    db.session.commit()
    flash('Goal added successfully!', 'success')
    return redirect(url_for('goals.view'))


@goals_bp.route('/<int:id>/complete', methods=['POST'])
def complete_goal(id):
    goal = Goal.query.get_or_404(id)
    goal.status = 'completed'
    goal.progress_percent = 100
    db.session.commit()
    flash('Goal completed!', 'success')
    return redirect(url_for('goals.view'))


@goals_bp.route('/<int:id>/delete', methods=['POST'])
def delete_goal(id):
    goal = Goal.query.get_or_404(id)
    db.session.delete(goal)
    db.session.commit()
    flash('Goal deleted.', 'info')
    return redirect(url_for('goals.view'))
