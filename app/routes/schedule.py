from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.schedule import ScheduleItem, StickyNote

schedule_bp = Blueprint('schedule', __name__)

DAYS_ORDER = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


@schedule_bp.route('/')
def view():
    items = ScheduleItem.query.all()
    sticky_notes = StickyNote.query.order_by(StickyNote.created_at.desc()).all()

    schedule_by_day = {day: [] for day in DAYS_ORDER}
    for item in items:
        if item.day_of_week.lower() in schedule_by_day:
            schedule_by_day[item.day_of_week.lower()].append(item)

    total_sessions = len(items)
    workout_days = len([d for d, items_list in schedule_by_day.items()
                        if any(i.item_type == 'workout' for i in items_list)])
    rest_days = len([d for d, items_list in schedule_by_day.items()
                     if any(i.item_type == 'rest' for i in items_list)])
    completed_sessions = len([i for i in items if i.item_type == 'workout'])
    progress_percent = round(workout_days / 7 * 100) if workout_days > 0 else 0

    return render_template('schedule.html',
        active_page='schedule',
        schedule_by_day=schedule_by_day,
        days_order=DAYS_ORDER,
        sticky_notes=sticky_notes,
        total_sessions=total_sessions,
        completed_sessions=completed_sessions,
        workout_days=workout_days,
        rest_days=rest_days,
        progress_percent=progress_percent,
    )


@schedule_bp.route('/add', methods=['POST'])
def add_item():
    name = request.form.get('name', '').strip()
    day = request.form.get('day', 'monday')
    time = request.form.get('time', '')
    details = request.form.get('details', '')
    item_type = request.form.get('type', 'workout')
    if not name:
        flash('Schedule item name is required.', 'error')
        return redirect(url_for('schedule.view'))
    item = ScheduleItem(day_of_week=day, time=time, name=name, details=details, item_type=item_type)
    db.session.add(item)
    db.session.commit()
    flash('Schedule item added!', 'success')
    return redirect(url_for('schedule.view'))


@schedule_bp.route('/notes/add', methods=['POST'])
def add_note():
    title = request.form.get('title', '').strip()
    content = request.form.get('content', '')
    color = request.form.get('color', 'yellow')
    if not title:
        flash('Note title is required.', 'error')
        return redirect(url_for('schedule.view'))
    note = StickyNote(title=title, content=content, color=color)
    db.session.add(note)
    db.session.commit()
    flash('Note added!', 'success')
    return redirect(url_for('schedule.view'))


@schedule_bp.route('/notes/<int:id>/delete', methods=['POST'])
def delete_note(id):
    note = StickyNote.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    flash('Note deleted.', 'info')
    return redirect(url_for('schedule.view'))
