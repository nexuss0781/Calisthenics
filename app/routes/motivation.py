from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.motivation import Motivation

motivation_bp = Blueprint('motivation', __name__)


@motivation_bp.route('/')
def view():
    category = request.args.get('category', '')
    query = Motivation.query
    if category:
        query = query.filter_by(category=category)
    motivations = query.order_by(Motivation.created_at.desc()).all()

    categories = ['video', 'book', 'quote', 'movie', 'podcast']

    return render_template('motivation.html',
        active_page='motivation',
        motivations=motivations,
        categories=categories,
        current_category=category,
    )


@motivation_bp.route('/add', methods=['POST'])
def add():
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '')
    category = request.form.get('category', 'video')
    author = request.form.get('author', '')
    duration_or_pages = request.form.get('duration_or_pages', '')
    if not title:
        flash('Title is required.', 'error')
        return redirect(url_for('motivation.view'))
    item = Motivation(title=title, description=description, category=category, author=author, duration_or_pages=duration_or_pages)
    db.session.add(item)
    db.session.commit()
    flash('Motivation added!', 'success')
    return redirect(url_for('motivation.view'))


@motivation_bp.route('/<int:id>/favorite', methods=['POST'])
def favorite(id):
    item = Motivation.query.get_or_404(id)
    item.is_favorite = not item.is_favorite
    db.session.commit()
    return redirect(url_for('motivation.view', category=request.args.get('category', '')))


@motivation_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    item = Motivation.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Item deleted.', 'info')
    return redirect(url_for('motivation.view', category=request.args.get('category', '')))
