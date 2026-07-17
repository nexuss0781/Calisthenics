import json
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.tournament import UserLevel, TournamentChallenge

tournament_bp = Blueprint('tournament', __name__)


@tournament_bp.route('/')
def view():
    user_level = UserLevel.query.first()
    challenges = TournamentChallenge.query.order_by(TournamentChallenge.level_required.asc()).all()

    xp_percent = 0
    level_history = []
    if user_level:
        xp_percent = round(user_level.current_xp / user_level.max_xp * 100) if user_level.max_xp > 0 else 0
        level_history = json.loads(user_level.level_history) if user_level.level_history else []

    for c in challenges:
        c.details_dict = json.loads(c.details) if c.details else {}

    return render_template('tournament.html',
        active_page='tournament',
        user_level=user_level,
        challenges=challenges,
        xp_percent=xp_percent,
        level_history_json=json.dumps(level_history),
        level_history_data=level_history,
    )


@tournament_bp.route('/join', methods=['POST'])
def join():
    user_level = UserLevel.query.first()
    if not user_level:
        user_level = UserLevel(current_level=1, rank_name='Beginner', current_xp=0, max_xp=1000)
        db.session.add(user_level)
    user_level.tournaments_participated += 1
    db.session.commit()
    flash('Joined tournament!', 'success')
    return redirect(url_for('tournament.view'))


@tournament_bp.route('/challenge/<int:id>/start', methods=['POST'])
def start_challenge(id):
    challenge = TournamentChallenge.query.get_or_404(id)
    if challenge.status == 'locked':
        flash('You need a higher level to unlock this challenge.', 'error')
    else:
        flash(f'Started: {challenge.title}!', 'success')
    return redirect(url_for('tournament.view'))
