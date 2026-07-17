from datetime import datetime
from app import db


class Goal(db.Model):
    __tablename__ = 'goals'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, default='')
    target_date = db.Column(db.Date)
    status = db.Column(db.String(20), default='not_started')  # in_progress/completed/not_started
    progress_percent = db.Column(db.Integer, default=0)
    progress_text = db.Column(db.String(100), default='')
    media_count_photos = db.Column(db.Integer, default=0)
    media_count_videos = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def status_label(self):
        labels = {
            'completed': 'Completed',
            'in_progress': 'In Progress',
            'not_started': 'Not Started',
        }
        return labels.get(self.status, self.status)

    def __repr__(self):
        return f'<Goal {self.title}>'
