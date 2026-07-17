from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.video import Video

videos_bp = Blueprint('videos', __name__)


@videos_bp.route('/')
def view():
    category = request.args.get('category', '')
    query = Video.query
    if category:
        query = query.filter_by(category=category)
    videos = query.order_by(Video.upload_date.desc()).all()

    categories = ['tutorial', 'workout', 'progress', 'motivation']

    return render_template('videos.html',
        active_page='videos',
        videos=videos,
        categories=categories,
        current_category=category,
    )


@videos_bp.route('/upload', methods=['POST'])
def upload():
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '')
    category = request.form.get('category', 'tutorial')
    if not title:
        flash('Video title is required.', 'error')
        return redirect(url_for('videos.view'))
    video = Video(title=title, description=description, category=category)
    db.session.add(video)
    db.session.commit()
    flash('Video uploaded!', 'success')
    return redirect(url_for('videos.view'))
