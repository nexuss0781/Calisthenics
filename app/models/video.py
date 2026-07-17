from datetime import datetime
from app import db


class Video(db.Model):
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, default='')
    category = db.Column(db.String(50), default='')  # tutorial/workout/progress/motivation
    duration = db.Column(db.String(20), default='')
    views = db.Column(db.String(20), default='0')
    likes = db.Column(db.Integer, default=0)
    upload_date = db.Column(db.Date)
    thumbnail_gradient = db.Column(db.String(200), default='')
    share_platforms = db.Column(db.Text, default='[]')  # JSON list
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Video {self.title}>'
