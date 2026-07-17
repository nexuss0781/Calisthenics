from flask import Blueprint, render_template
from app import db
from app.models.workout import Workout, Exercise
from app.models.goal import Goal
from app.models.health import HealthRecord

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    total_workouts = Workout.query.filter_by(completed=True).count()
    monthly_workouts = Workout.query.filter_by(completed=True).count()
    goals_achieved = Goal.query.filter_by(status='completed').count()
    total_goals = Goal.query.count()
    goals_percent = round(goals_achieved / total_goals * 100) if total_goals > 0 else 0
    latest_health = HealthRecord.query.order_by(HealthRecord.date.desc()).first()
    recent_workouts = Workout.query.order_by(Workout.scheduled_date.desc()).limit(3).all()

    return render_template('index.html',
        active_page='home',
        total_workouts=total_workouts,
        monthly_workouts=monthly_workouts,
        goals_achieved=goals_achieved,
        total_goals=total_goals,
        goals_percent=goals_percent,
        latest_weight=latest_health.weight if latest_health else 0,
        bmi=latest_health.bmi if latest_health else 0,
        recent_workouts=recent_workouts,
    )
