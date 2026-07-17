from datetime import datetime
from app import db


class ScheduleItem(db.Model):
    __tablename__ = 'schedule_items'

    id = db.Column(db.Integer, primary_key=True)
    day_of_week = db.Column(db.String(10), nullable=False)  # monday-sunday
    time = db.Column(db.String(10), default='')
    name = db.Column(db.String(100), nullable=False)
    details = db.Column(db.Text, default='')
    item_type = db.Column(db.String(20), default='workout')  # workout/rest/planned
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<ScheduleItem {self.name}>'


class StickyNote(db.Model):
    __tablename__ = 'sticky_notes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, default='')
    color = db.Column(db.String(20), default='yellow')  # yellow/orange/pink/green
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<StickyNote {self.title}>'
