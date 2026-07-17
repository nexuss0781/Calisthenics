from datetime import datetime
from app import db


class Plan(db.Model):
    __tablename__ = 'plans'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    plan_type = db.Column(db.String(50), nullable=False)  # strength/skill/endurance/flexibility/recovery
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    description = db.Column(db.Text, default='')
    status = db.Column(db.String(20), default='upcoming')  # completed/in_progress/upcoming
    progress_percent = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Plan {self.title}>'
