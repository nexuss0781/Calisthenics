from datetime import datetime
from app import db


class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)  # beginner/intermediate/advanced
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    rest_minutes = db.Column(db.Float, nullable=False)
    form_instructions = db.Column(db.Text, default='[]')  # JSON list
    workout_days = db.Column(db.Text, default='[]')  # JSON list of day cards
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Exercise {self.name}>'


class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    exercises_used = db.Column(db.Text, default='')  # comma-separated
    scheduled_date = db.Column(db.DateTime)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Workout {self.name}>'
