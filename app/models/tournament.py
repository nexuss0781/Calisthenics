from datetime import datetime
from app import db


class TournamentChallenge(db.Model):
    __tablename__ = 'tournament_challenges'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    level_required = db.Column(db.Integer, default=1)
    status = db.Column(db.String(20), default='active')  # active/completed/locked
    details = db.Column(db.Text, default='{}')  # JSON: pushups, sets, rest
    time_limit = db.Column(db.String(50), default='')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<TournamentChallenge {self.title}>'


class UserLevel(db.Model):
    __tablename__ = 'user_levels'

    id = db.Column(db.Integer, primary_key=True)
    current_level = db.Column(db.Integer, default=1)
    rank_name = db.Column(db.String(50), default='Beginner')
    current_xp = db.Column(db.Integer, default=0)
    max_xp = db.Column(db.Integer, default=1000)
    tournaments_participated = db.Column(db.Integer, default=0)
    wins = db.Column(db.Integer, default=0)
    global_rank = db.Column(db.Integer, default=0)
    win_streak = db.Column(db.Integer, default=0)
    level_history = db.Column(db.Text, default='[]')  # JSON: monthly levels
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<UserLevel {self.current_level}>'
