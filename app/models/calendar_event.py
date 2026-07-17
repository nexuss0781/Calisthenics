from datetime import datetime
from app import db


class CalendarEvent(db.Model):
    __tablename__ = 'calendar_events'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    event_type = db.Column(db.String(20), default='workout')  # workout/rest/planned/tournament
    name = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<CalendarEvent {self.name}>'
