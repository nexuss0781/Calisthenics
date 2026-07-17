from datetime import datetime
from app import db


class HealthRecord(db.Model):
    __tablename__ = 'health_records'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    weight = db.Column(db.Float, nullable=True)
    height = db.Column(db.Float, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(20), nullable=True)
    body_fat = db.Column(db.Float, nullable=True)
    performance_notes = db.Column(db.Text, default='')
    bmi = db.Column(db.Float, nullable=True)  # calculated
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def calculate_bmi(self):
        if self.weight and self.height:
            height_m = self.height / 100
            self.bmi = round(self.weight / (height_m ** 2), 1)
        return self.bmi

    def __repr__(self):
        return f'<HealthRecord {self.date}>'


class HealthPlanItem(db.Model):
    __tablename__ = 'health_plan_items'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, default='')
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<HealthPlanItem {self.title}>'
