import json
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.workout import Exercise

workouts_bp = Blueprint('workouts', __name__)


@workouts_bp.route('/')
def list():
    exercises = Exercise.query.order_by(Exercise.created_at.desc()).all()
    for ex in exercises:
        ex.form_list = json.loads(ex.form_instructions) if ex.form_instructions else []
        ex.days = json.loads(ex.workout_days) if ex.workout_days else []
    return render_template('workouts.html', active_page='workouts', exercises=exercises)


@workouts_bp.route('/add', methods=['POST'])
def add_exercise():
    name = request.form.get('name', '').strip()
    difficulty = request.form.get('difficulty', 'beginner')
    sets = request.form.get('sets', 3, type=int)
    reps = request.form.get('reps', 10, type=int)
    rest = request.form.get('rest', 2, type=float)
    if not name:
        flash('Exercise name is required.', 'error')
        return redirect(url_for('workouts.list'))
    exercise = Exercise(name=name, difficulty=difficulty, sets=sets, reps=reps, rest_minutes=rest)
    db.session.add(exercise)
    db.session.commit()
    flash('Exercise added successfully!', 'success')
    return redirect(url_for('workouts.list'))


@workouts_bp.route('/<int:id>/delete', methods=['POST'])
def delete_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    db.session.delete(exercise)
    db.session.commit()
    flash('Exercise deleted.', 'info')
    return redirect(url_for('workouts.list'))
