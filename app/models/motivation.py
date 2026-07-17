from datetime import datetime
from app import db


class Motivation(db.Model):
    __tablename__ = 'motivation'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, default='')
    category = db.Column(db.String(50), default='')  # video/book/quote/movie/podcast
    author = db.Column(db.String(100), default='')
    duration_or_pages = db.Column(db.String(50), default='')
    gradient = db.Column(db.String(200), default='')
    is_favorite = db.Column(db.Boolean, default=False)
    url = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Motivation {self.title}>'
