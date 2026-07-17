import json
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from datetime import date, datetime
from app import db
from app.models.calendar_event import CalendarEvent

calendar_bp = Blueprint('calendar', __name__)


@calendar_bp.route('/')
def view():
    events = CalendarEvent.query.order_by(CalendarEvent.date.asc()).all()
    total_workouts = CalendarEvent.query.filter_by(event_type='workout').count()
    completed_count = CalendarEvent.query.filter(
        CalendarEvent.date <= date.today(), CalendarEvent.event_type == 'workout'
    ).count()
    planned_count = CalendarEvent.query.filter(
        CalendarEvent.date > date.today(), CalendarEvent.event_type == 'workout'
    ).count()
    rest_count = CalendarEvent.query.filter_by(event_type='rest').count()

    total = total_workouts + rest_count if total_workouts + rest_count > 0 else 1
    progress_percent = round(completed_count / total * 100) if total > 0 else 0

    return render_template('calendar.html',
        active_page='calendar',
        events=events,
        total_workouts=total_workouts,
        completed_count=completed_count,
        planned_count=planned_count,
        rest_count=rest_count,
        progress_percent=progress_percent,
    )


@calendar_bp.route('/api/events')
def api_events():
    events = CalendarEvent.query.all()
    return jsonify([{
        'date': e.date.isoformat() if e.date else '',
        'type': e.event_type,
        'name': e.name
    } for e in events])


@calendar_bp.route('/add', methods=['POST'])
def add_event():
    name = request.form.get('name', '').strip()
    event_date_str = request.form.get('date', '')
    event_type = request.form.get('type', 'workout')
    if not name or not event_date_str:
        flash('Event name and date are required.', 'error')
        return redirect(url_for('calendar.view'))
    event_date = date.fromisoformat(event_date_str)
    event = CalendarEvent(date=event_date, event_type=event_type, name=name)
    db.session.add(event)
    db.session.commit()
    flash('Event added!', 'success')
    return redirect(url_for('calendar.view'))


@calendar_bp.route('/plan/<int:id>/delete', methods=['POST'])
def delete_event(id):
    event = CalendarEvent.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    flash('Event deleted.', 'info')
    return redirect(url_for('calendar.view'))
