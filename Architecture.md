# Architecture.md - Calisthenics Dashboard: Static-to-Dynamic Conversion

## 1. Current State Analysis

### 1.1 Existing Structure
```
Calisthenics-Prototype/
├── index.html          (662 lines)  - Dashboard (SPA-style with all pages embedded)
├── Goals.html          (1105 lines) - Goals management
├── Plan.html           (1052 lines) - Training plans
├── Schedule.html       (966 lines)  - Weekly schedule
├── Tournament.html     (940 lines)  - Tournament/gamification
├── calander.html       (927 lines)  - Calendar view
├── Motivation.html     (1036 lines) - Motivational content
├── Health.html         (980 lines)  - Health metrics
├── videos.html         (1191 lines) - Video library
├── Workouts.html       (1037 lines) - Exercise catalog
└── README.md
```

### 1.2 Key Observations
- **10 standalone HTML files**, each self-contained with inline `<style>` and `<script>`
- **Massive CSS duplication**: Every file repeats ~300+ lines of identical sidebar/layout CSS
- **Two architecture patterns exist**:
  - `index.html`: SPA-style (all pages as `<div>` sections toggled by JS)
  - All other files: Separate full-page HTML files, each with its own sidebar
- **All data is hardcoded** in HTML - no dynamic content
- **JS interactivity** includes: modals, form validation, category filtering, card expansion, calendar rendering, drag-and-drop file upload, animations
- **No external CSS/JS files** - everything is inline
- **No backend, no database, no Python**

---

## 2. Target Architecture

### 2.1 Technology Stack
| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3.x + Flask |
| **Templating** | Jinja2 (bundled with Flask) |
| **Database** | SQLite (via SQLAlchemy ORM) for simplicity, upgradeable to PostgreSQL |
| **Static Files** | Extracted CSS + JS served by Flask |
| **Form Handling** | Flask-WTF or plain Flask request handling |

### 2.2 Directory Structure (Target)
```
Calisthenics-Prototype/
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── config.py                # Configuration (DB URI, secret key, etc.)
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py              # User model (future auth)
│   │   ├── workout.py           # Workout/Exercise models
│   │   ├── goal.py              # Goal model
│   │   ├── plan.py              # Training plan model
│   │   ├── schedule.py          # Schedule/Weekly plan model
│   │   ├── health.py            # Health metrics model
│   │   ├── tournament.py        # Tournament/Challenge model
│   │   ├── video.py             # Video model
│   │   ├── motivation.py        # Motivation content model
│   │   └── calendar_event.py    # Calendar event model
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main.py              # Dashboard/home routes
│   │   ├── workouts.py          # Workout CRUD routes
│   │   ├── goals.py             # Goal CRUD routes
│   │   ├── plan.py              # Plan CRUD routes
│   │   ├── schedule.py          # Schedule routes
│   │   ├── health.py            # Health metrics routes + export
│   │   ├── tournament.py        # Tournament routes
│   │   ├── calendar.py          # Calendar routes
│   │   ├── motivation.py        # Motivation content routes
│   │   └── videos.py            # Video routes
│   ├── services/
│   │   ├── __init__.py
│   │   ├── dashboard_service.py # Aggregates stats for dashboard
│   │   ├── calendar_service.py  # Calendar date/event logic
│   │   └── health_service.py    # BMI calc, export logic
│   └── templates/
│       ├── base.html            # Master layout (sidebar + CSS + JS)
│       ├── partials/
│       │   ├── _sidebar.html    # Sidebar navigation component
│       │   ├── _header.html     # Page header with title + action button
│       │   ├── _modal.html      # Reusable modal wrapper
│       │   ├── _stats_card.html # Reusable stat card component
│       │   ├── _progress_bar.html # Reusable progress bar
│       │   └── _footer.html     # Optional footer
│       ├── index.html           # Dashboard page
│       ├── workouts.html        # Workouts page
│       ├── calendar.html        # Calendar page
│       ├── schedule.html        # Schedule page
│       ├── health.html          # Health page
│       ├── plan.html            # Plan page
│       ├── tournament.html      # Tournament page
│       ├── goals.html           # Goals page
│       ├── motivation.html      # Motivation page
│       └── videos.html          # Videos page
├── static/
│   ├── css/
│   │   ├── main.css             # Extracted shared styles (sidebar, layout, variables)
│   │   ├── dashboard.css        # Dashboard-specific styles
│   │   ├── workouts.css         # Workouts page styles
│   │   ├── calendar.css         # Calendar page styles
│   │   ├── schedule.css         # Schedule page styles
│   │   ├── health.css           # Health page styles
│   │   ├── plan.css             # Plan page styles
│   │   ├── tournament.css       # Tournament page styles
│   │   ├── goals.css            # Goals page styles
│   │   ├── motivation.css       # Motivation page styles
│   │   └── videos.css           # Videos page styles
│   ├── js/
│   │   ├── main.js              # Shared JS (sidebar, modal utils)
│   │   ├── calendar.js          # Calendar rendering logic
│   │   ├── workouts.js          # Workout card expansion, forms
│   │   ├── goals.js             # Goal CRUD UI interactions
│   │   ├── schedule.js          # Schedule drag-drop, sticky notes
│   │   ├── health.js            # Health charts, export
│   │   ├── motivation.js        # Category filtering
│   │   ├── videos.js            # Video player, file drop
│   │   └── tournament.js        # Challenge interactions
│   └── images/                  # Placeholder for uploaded images
├── migrations/                  # SQLAlchemy migrations (if using Flask-Migrate)
├── instance/
│   └── calisthenics.db          # SQLite database file
├── requirements.txt             # Python dependencies
├── run.py                       # Application entry point
├── seed.py                      # Database seeder (populates initial data from HTML)
└── docs/
    ├── Architecture.md
    ├── Phase.md
    └── Todo.md
```

---

## 3. Data Models

### 3.1 Core Entities

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Workout    │────>│  Exercise    │     │    Goal      │
│  (session)   │     │  (catalog)   │     │              │
└─────────────┘     └──────────────┘     └─────────────┘
       │                    │                    │
       v                    v                    v
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  Schedule    │     │  Plan        │     │  Health      │
│  (weekly)    │     │  (training)  │     │  (metrics)   │
└─────────────┘     └──────────────┘     └─────────────┘
       │                    │                    │
       v                    v                    v
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  Calendar    │     │ Tournament   │     │  Video       │
│  (events)    │     │ (challenges) │     │  (library)   │
└─────────────┘     └──────────────┘     └─────────────┘
                           │
                           v
                    ┌──────────────┐
                    │ Motivation   │
                    │ (content)    │
                    └──────────────┘
```

### 3.2 Model Definitions

```python
# Exercise (Workouts catalog)
class Exercise:
    id: int (PK)
    name: str
    difficulty: str  # beginner/intermediate/advanced
    sets: int
    reps: int
    rest_minutes: float
    form_instructions: text (JSON list)
    workout_days: text (JSON list of day cards)
    created_at: datetime

# Workout (session log - from Dashboard "Recent Workouts")
class Workout:
    id: int (PK)
    name: str
    exercises_used: str  # comma-separated or JSON
    scheduled_date: datetime
    completed: bool
    created_at: datetime

# Goal
class Goal:
    id: int (PK)
    title: str
    description: text
    target_date: date
    status: str  # in_progress/completed/not_started
    progress_percent: int
    progress_text: str  # e.g., "25/60 seconds"
    media_count_photos: int
    media_count_videos: int
    created_at: datetime

# Plan (Training Plan)
class Plan:
    id: int (PK)
    title: str
    plan_type: str  # strength/skill/endurance/flexibility/recovery
    start_date: date
    end_date: date
    description: text
    status: str  # completed/in_progress/upcoming
    progress_percent: int
    created_at: datetime

# Schedule (Weekly Schedule items)
class ScheduleItem:
    id: int (PK)
    day_of_week: str  # monday-sunday
    time: str
    name: str
    details: str
    item_type: str  # workout/rest/planned
    created_at: datetime

# CalendarEvent
class CalendarEvent:
    id: int (PK)
    date: date
    event_type: str  # workout/rest/planned/tournament
    name: str
    created_at: datetime

# HealthRecord
class HealthRecord:
    id: int (PK)
    date: date
    weight: float
    height: float
    age: int
    gender: str
    body_fat: float (nullable)
    performance_notes: text
    bmi: float (calculated)
    created_at: datetime

# HealthPlanItem
class HealthPlanItem:
    id: int (PK)
    title: str
    description: str
    completed: bool
    created_at: datetime

# TournamentChallenge
class TournamentChallenge:
    id: int (PK)
    title: str
    level_required: int
    status: str  # active/completed/locked
    details: text (JSON: pushups, sets, rest)
    time_limit: str
    created_at: datetime

# UserLevel (gamification)
class UserLevel:
    id: int (PK)
    current_level: int
    rank_name: str
    current_xp: int
    max_xp: int
    tournaments_participated: int
    wins: int
    global_rank: int
    win_streak: int
    level_history: text (JSON: monthly levels)
    updated_at: datetime

# Video
class Video:
    id: int (PK)
    title: str
    description: text
    category: str  # tutorial/workout/progress/motivation
    duration: str
    views: str
    likes: int
    upload_date: date
    thumbnail_gradient: str  # CSS gradient for placeholder
    share_platforms: text (JSON list)
    created_at: datetime

# Motivation
class Motivation:
    id: int (PK)
    title: str
    description: text
    category: str  # video/book/quote/movie/podcast
    author: str
    duration_or_pages: str
    gradient: str  # CSS gradient for card image
    is_favorite: bool
    url: str (nullable)
    created_at: datetime

# StickyNote (from Schedule page)
class StickyNote:
    id: int (PK)
    title: str
    content: text
    color: str  # yellow/orange/pink/green
    created_at: datetime
```

---

## 4. Route Architecture

### 4.1 URL Mapping

| URL | Method | Template | Description |
|-----|--------|----------|-------------|
| `/` | GET | `index.html` | Dashboard home |
| `/workouts` | GET | `workouts.html` | List all exercises |
| `/workouts/add` | POST | - | Add new exercise |
| `/workouts/<id>/edit` | POST | - | Edit exercise |
| `/workouts/<id>/delete` | POST | - | Delete exercise |
| `/calendar` | GET | `calendar.html` | Calendar view |
| `/calendar/add` | POST | - | Add calendar event |
| `/calendar/api/events` | GET | JSON | Get events for JS calendar |
| `/schedule` | GET | `schedule.html` | Weekly schedule |
| `/schedule/add` | POST | - | Add schedule item |
| `/schedule/notes` | GET/POST | - | Sticky notes CRUD |
| `/health` | GET | `health.html` | Health metrics |
| `/health/add` | POST | - | Add health record |
| `/health/export` | GET | TXT file | Export health data |
| `/plan` | GET | `plan.html` | Training plans |
| `/plan/add` | POST | - | Add new plan |
| `/plan/<id>/edit` | POST | - | Edit plan |
| `/plan/<id>/delete` | POST | - | Delete plan |
| `/tournament` | GET | `tournament.html` | Tournament page |
| `/tournament/join` | POST | - | Join tournament |
| `/goals` | GET | `goals.html` | Goals page |
| `/goals/add` | POST | - | Add new goal |
| `/goals/<id>/complete` | POST | - | Toggle completion |
| `/goals/<id>/delete` | POST | - | Delete goal |
| `/motivation` | GET | `motivation.html` | Motivation page |
| `/motivation/add` | POST | - | Add motivation content |
| `/motivation/<id>/favorite` | POST | - | Toggle favorite |
| `/motivation/<id>/delete` | POST | - | Delete item |
| `/videos` | GET | `videos.html` | Videos page |
| `/videos/upload` | POST | - | Upload video |
| `/videos/<id>/player` | GET | - | Video player modal data |

### 4.2 Blueprint Structure
```python
# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    from app.routes.main import main_bp
    from app.routes.workouts import workouts_bp
    from app.routes.calendar import calendar_bp
    from app.routes.schedule import schedule_bp
    from app.routes.health import health_bp
    from app.routes.plan import plan_bp
    from app.routes.tournament import tournament_bp
    from app.routes.goals import goals_bp
    from app.routes.motivation import motivation_bp
    from app.routes.videos import videos_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(workouts_bp, url_prefix='/workouts')
    app.register_blueprint(calendar_bp, url_prefix='/calendar')
    app.register_blueprint(schedule_bp, url_prefix='/schedule')
    app.register_blueprint(health_bp, url_prefix='/health')
    app.register_blueprint(plan_bp, url_prefix='/plan')
    app.register_blueprint(tournament_bp, url_prefix='/tournament')
    app.register_blueprint(goals_bp, url_prefix='/goals')
    app.register_blueprint(motivation_bp, url_prefix='/motivation')
    app.register_blueprint(videos_bp, url_prefix='/videos')

    return app
```

---

## 5. Template Architecture

### 5.1 Base Template (`base.html`)
The master layout that every page extends:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Calisthenics{% endblock %}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
    {% block extra_css %}{% endblock %}
</head>
<body>
    <div class="container">
        {% include 'partials/_sidebar.html' %}
        <div class="main-content">
            {% block content %}{% endblock %}
        </div>
    </div>
    {% block modals %}{% endblock %}
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

### 5.2 Sidebar Partial (`_sidebar.html`)
```html
<div class="sidebar">
    <div class="logo">
        <h2><i class="fas fa-dumbbell"></i> <span>Calisthenics</span></h2>
    </div>
    <ul class="nav-links">
        {% set nav_items = [
            ('home', 'fa-home', 'Home', 'main.index'),
            ('workouts', 'fa-running', 'Workouts', 'workouts.list'),
            ('calendar', 'fa-calendar-alt', 'Calendar', 'calendar.view'),
            ('schedule', 'fa-clock', 'Schedule', 'schedule.view'),
            ('health', 'fa-heartbeat', 'Health', 'health.view'),
            ('plan', 'fa-tasks', 'Plan', 'plan.view'),
            ('tournament', 'fa-trophy', 'Tournament', 'tournament.view'),
            ('goals', 'fa-bullseye', 'Goals', 'goals.view'),
            ('motivation', 'fa-fire', 'Motivation', 'motivation.view'),
            ('videos', 'fa-video', 'Videos', 'videos.view')
        ] %}
        {% for page_id, icon, label, route in nav_items %}
        <li>
            <a href="{{ url_for(route) }}"
               class="{% if active_page == page_id %}active{% endif %}"
               data-page="{{ page_id }}">
                <i class="fas {{ icon }}"></i> <span>{{ label }}</span>
            </a>
        </li>
        {% endfor %}
    </ul>
</div>
```

### 5.3 Template Inheritance Example (Goals)
```html
{% extends "base.html" %}

{% block title %}Goals - Calisthenics{% endblock %}

{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/goals.css') }}">
{% endblock %}

{% block content %}
<div class="header">
    <h1>Goals</h1>
    <div class="header-actions">
        <button id="addGoalBtn"><i class="fas fa-plus"></i> Add Goal</button>
    </div>
</div>

<div class="goals-layout">
    <!-- Progress Overview (static layout, dynamic stats) -->
    <div class="progress-card">
        <div class="card-header">
            <h2 class="card-title">Goal Progress</h2>
        </div>
        <div class="progress-stats">
            <div class="stat-card">
                <div class="stat-label">Completed Goals</div>
                <div class="stat-value completed">{{ completed_goals }}</div>
                <div class="stat-label">Out of {{ total_goals }}</div>
            </div>
            <!-- ... -->
        </div>
    </div>

    <!-- Goals List (dynamic loop) -->
    <div class="goals-list-card">
        <h2 class="goals-title">Your Goals</h2>
        {% for goal in goals %}
        <div class="goal-item {{ 'completed' if goal.status == 'completed' }}">
            <div class="goal-header">
                <div>
                    <div class="goal-title">{{ goal.title }}</div>
                    <div class="goal-status status-{{ goal.status }}">{{ goal.status_label }}</div>
                </div>
            </div>
            <div class="goal-description">{{ goal.description }}</div>
            <div class="goal-progress">
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {{ goal.progress_percent }}%;"></div>
                </div>
                <div class="progress-text">
                    <span>{{ goal.progress_text }}</span>
                    <span>Target: {{ goal.target_date.strftime('%b %d, %Y') }}</span>
                </div>
            </div>
            <!-- ... -->
        </div>
        {% endfor %}
    </div>
</div>
{% endblock %}
```

---

## 6. Static Asset Extraction Strategy

### 6.1 CSS Separation Plan

| File | Source | Content |
|------|--------|---------|
| `main.css` | Extracted from all 10 HTML files | CSS variables, base reset, sidebar, layout, header, responsive breakpoints, shared card styles |
| `dashboard.css` | `index.html` | `.dashboard-grid`, `.stat-number`, `.workout-list` |
| `workouts.css` | `Workouts.html` | `.workouts-grid`, `.exercise-card`, `.expanded-content`, `.workout-days` |
| `calendar.css` | `calander.html` | `.calendar-layout`, `.calendar-card`, `.calendar-grid`, `.plan-card` |
| `schedule.css` | `Schedule.html` | `.schedule-layout`, `.weekly-schedule`, `.day-column`, `.sticky-*` |
| `health.css` | `Health.html` | `.health-layout`, `.health-card`, `.basic-info-form`, `.chart-*` |
| `plan.css` | `Plan.html` | `.plan-layout`, `.plan-card`, `.plan-stats`, `.timeline-*`, `.calendar-integration` |
| `tournament.css` | `Tournament.html` | `.level-card`, `.challenge-*`, `.xp-*`, `.level-graph` |
| `goals.css` | `Goals.html` | `.goals-layout`, `.goal-item`, `.progress-chart`, `.gallery-*`, `.add-goal-modal` |
| `motivation.css` | `Motivation.html` | `.motivation-grid`, `.motivation-card`, `.card-image.*`, `.categories-nav` |
| `videos.css` | `videos.html` | `.videos-grid`, `.video-card`, `.video-thumbnail`, `.video-player-*`, `.upload-*` |

### 6.2 JavaScript Separation Plan

| File | Source | Content |
|------|--------|---------|
| `main.js` | All files | Sidebar navigation, modal open/close utilities, shared helpers |
| `calendar.js` | `calander.html` | Calendar grid generation, month navigation, event rendering |
| `workouts.js` | `Workouts.html` | Card expansion, add exercise form, edit/delete actions |
| `goals.js` | `Goals.html` | Add goal modal, file upload preview, goal actions |
| `schedule.js` | `Schedule.html` | Schedule modal, sticky note interactions |
| `health.js` | `Health.html` | Health record modal, BMI calculation, data export to txt |
| `motivation.js` | `Motivation.html` | Category filtering, card actions |
| `videos.js` | `videos.html` | Video player modal, file drag-drop, category filtering, social sharing |
| `tournament.js` | `Tournament.html` | Join tournament modal, challenge button interactions |

---

## 7. Data Seeding Strategy

A `seed.py` script will populate the database with the exact data currently hardcoded in the HTML files. This ensures the dynamic app renders identically to the static prototype on first run.

```python
# Example: Seeding exercises from Workouts.html
exercises = [
    {"name": "Push-ups", "difficulty": "beginner", "sets": 3, "reps": 15, "rest_minutes": 2,
     "form_instructions": ["Start in plank position...", ...], "workout_days": [...]},
    {"name": "Pull-ups", "difficulty": "intermediate", "sets": 4, "reps": 8, "rest_minutes": 3, ...},
    {"name": "Muscle-ups", "difficulty": "advanced", "sets": 3, "reps": 5, "rest_minutes": 4, ...},
    {"name": "Handstand Push-ups", "difficulty": "advanced", "sets": 3, "reps": 6, "rest_minutes": 3, ...},
    {"name": "Squats", "difficulty": "beginner", "sets": 4, "reps": 20, "rest_minutes": 1.5, ...},
    {"name": "Lunges", "difficulty": "intermediate", "sets": 3, "reps": 12, "rest_minutes": 2, ...},
]
```

---

## 8. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **SPA vs Multi-page** | Multi-page with Flask routes | Matches the existing separate HTML files pattern; simpler Jinja2 conversion |
| **Database** | SQLite | Zero-config, file-based, perfect for prototype phase |
| **ORM** | SQLAlchemy | Clean model definitions, easy migration later |
| **CSS Strategy** | Extract to static files, keep identical styles | Zero frontend change guarantee |
| **JS Strategy** | Extract to static files, keep identical behavior | Forms POST to Flask routes instead of `alert()` |
| **Form Handling** | Server-side POST with redirect | Standard Flask pattern, preserves all current form fields |
| **File Uploads** | Flask `request.files` + save to `static/images/` | Simple for prototype, upgradeable to cloud storage |
| **Session Data** | Flask sessions | For any temporary state (current month in calendar, etc.) |

---

## 9. Conversion Mapping (HTML -> Dynamic)

| Static Element | Dynamic Replacement |
|----------------|---------------------|
| Hardcoded stats (e.g., "24" workouts) | `{{ stats.total_workouts }}` from DB query |
| Hardcoded workout list items | `{% for workout in workouts %}` loop |
| Hardcoded calendar days | Python `calendar` module + JS rendering with DB events |
| Hardcoded goal progress bars | `style="width: {{ goal.progress_percent }}%;"` |
| Hardcoded exercise cards | `{% for exercise in exercises %}` loop |
| `alert()` on form submit | `POST` to Flask route, flash message, redirect |
| Static sidebar active state | `class="{% if active_page == 'X' %}active{% endif %}"` |
| JS-generated calendar | Server provides events JSON, JS renders grid |
| File upload `alert()` | Actual file save to disk, record in DB |
| Export to txt | Flask response with `Content-Disposition: attachment` |

---

## 10. Visual Regression Guarantee

To ensure **zero frontend change**, the conversion follows these rules:

1. **CSS is extracted verbatim** - no style modifications, only moved to `.css` files
2. **HTML structure is preserved** - Jinja2 tags are inserted INTO existing markup, not replacing it
3. **All class names remain identical** - no renaming, no restructuring
4. **Inline styles are preserved** where they exist (e.g., `style="width: 100%;"`)
5. **Responsive breakpoints remain untouched**
6. **Font Awesome CDN link preserved**
7. **Modal markup preserved** - only form `action` attributes change
8. **JS behavior preserved** - only `alert()` calls replaced with form submissions
