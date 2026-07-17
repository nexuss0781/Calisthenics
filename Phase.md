# Phase.md - Calisthenics Dashboard: Conversion Phase Breakdown

## Overview

This document breaks the static-to-dynamic conversion into **6 phases**, ordered by dependency. Each phase builds on the previous one. The total estimated effort is **~40-50 hours** of development.

```
Phase 1: Foundation          ████░░░░░░░░░░░░░░░░  ~8 hrs
Phase 2: CSS/JS Extraction   ████████░░░░░░░░░░░░  ~6 hrs
Phase 3: Core Pages          ████████████████░░░░  ~12 hrs
Phase 4: Advanced Pages      ████████████████████  ~10 hrs
Phase 5: Form Processing     ████████░░░░░░░░░░░░  ~6 hrs
Phase 6: Polish & Seed       ████░░░░░░░░░░░░░░░░  ~4 hrs
```

---

## Phase 1: Foundation Setup

**Goal:** Establish the Flask project skeleton, database models, and base template.

**Duration:** ~8 hours

### Deliverables
- [ ] Flask app with application factory pattern
- [ ] SQLite database with SQLAlchemy ORM
- [ ] All 12 data models defined and created
- [ ] `base.html` template with sidebar navigation
- [ ] `_sidebar.html` partial with dynamic active state
- [ ] Configuration file (`config.py`)
- [ ] `requirements.txt` with all dependencies
- [ ] Application entry point (`run.py`)

### Key Activities

| # | Activity | Details |
|---|----------|---------|
| 1.1 | Project scaffolding | Create `app/`, `static/`, `templates/` directories. Initialize Flask app factory. |
| 1.2 | Config setup | `Config` class with `SECRET_KEY`, `SQLALCHEMY_DATABASE_URI`, `UPLOAD_FOLDER` |
| 1.3 | Model definitions | Define all 12 models in `app/models/` (see Architecture.md Section 3.2) |
| 1.4 | Database initialization | `db.create_all()` in app factory, verify all tables created |
| 1.5 | Base template | Create `base.html` with `<!DOCTYPE>`, `<head>`, sidebar `{% include %}`, content `{% block %}` |
| 1.6 | Sidebar partial | Extract sidebar HTML from any HTML file, add Jinja2 active state logic |
| 1.7 | Route stubs | Create all 10 blueprint files with placeholder `@bp.route('/')` returning rendered templates |
| 1.8 | Verify skeleton | Run `flask run`, confirm all 10 pages render with correct sidebar navigation |

### Exit Criteria
- `flask run` starts without errors
- All 10 pages render with the sidebar
- Sidebar navigation links work between pages
- Database file `instance/calisthenics.db` exists with all tables

---

## Phase 2: CSS & JS Extraction

**Goal:** Extract all inline CSS and JS from the 10 HTML files into static files. Zero visual change.

**Duration:** ~6 hours

### Deliverables
- [ ] `static/css/main.css` - shared styles extracted from all files
- [ ] 9 page-specific CSS files
- [ ] `static/js/main.js` - shared JS utilities
- [ ] 8 page-specific JS files
- [ ] `base.html` updated with `<link>` and `<script>` tags
- [ ] Visual verification: every page looks identical to original

### Key Activities

| # | Activity | Details |
|---|----------|---------|
| 2.1 | Extract shared CSS | Copy CSS from `index.html` `<style>` block. Identify lines repeated across all 10 files: CSS variables (`:root`), sidebar styles, layout styles, header styles, responsive media queries. Place in `main.css`. |
| 2.2 | Extract page CSS | For each of the 9 remaining pages, copy the non-shared CSS into its own file (e.g., `goals.css`, `workouts.css`). |
| 2.3 | Extract shared JS | From `index.html`, extract the SPA navigation JS into `main.js`. Also extract any shared modal open/close patterns. |
| 2.4 | Extract page JS | For each page, copy its `<script>` content to a separate `.js` file (e.g., `calendar.js`, `workouts.js`). |
| 2.5 | Update base.html | Add `<link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">` and all page-specific CSS `{% block extra_css %}` |
| 2.6 | Update page templates | Each page template adds `{% block extra_css %}` and `{% block extra_js %}` for its specific files |
| 2.7 | Visual regression test | Open each page in browser side-by-side with original HTML files. Confirm pixel-perfect match. |

### CSS Extraction Map

```
From index.html:
  -> main.css (lines 9-340: variables, reset, sidebar, layout, header, cards, responsive)
  -> dashboard.css (lines 142-247: .dashboard-grid, .stat-number, .workout-list)

From Goals.html:
  -> goals.css (everything not in main.css: .goals-layout, .progress-card, .goal-item, .modal, .gallery)

From Plan.html:
  -> plan.css (.plan-layout, .plan-card, .plan-stats, .timeline-*, .calendar-integration, .modal)

... (similar for all 10 files)
```

### JS Extraction Map

```
From index.html:
  -> main.js (SPA navigation: navLinks click handler, page-content toggle)

From Goals.html:
  -> goals.js (modal open/close, file upload, save goal, goal actions)

From calander.html:
  -> calendar.js (generateCalendar, formatDate, createDayElement, month nav, add plan modal)

... (similar for all files)
```

### Exit Criteria
- All 10 pages load with CSS from static files (no inline `<style>`)
- All JS loaded from static files (no inline `<script>`)
- Visual comparison shows no differences
- Browser console has no 404 errors for CSS/JS files

---

## Phase 3: Core Pages with Dynamic Data

**Goal:** Convert the 4 most data-heavy pages to render from the database.

**Duration:** ~12 hours

### 3A: Dashboard (Home) Page

| Activity | Details |
|----------|---------|
| Dashboard service | Query total workouts count, monthly workouts, goals stats, weight, recent workouts |
| Route handler | `GET /` queries DB, passes stats + lists to template |
| Template update | Replace hardcoded numbers with `{{ stats.total_workouts }}`, loop over `{{ recent_workouts }}` |

**Data flow:**
```
Dashboard Route -> DashboardService.get_dashboard_data()
  -> total_workouts = Workout.query.count()
  -> monthly_workouts = Workout.query.filter(month).count()
  -> goals_achieved = Goal.query.filter(status='completed').count()
  -> total_goals = Goal.query.count()
  -> latest_health = HealthRecord.query.order_by(date.desc()).first()
  -> recent_workouts = Workout.query.order_by(date.desc()).limit(3).all()
  -> Pass all to index.html template
```

### 3B: Workouts Page

| Activity | Details |
|----------|---------|
| Route handler | `GET /workouts` queries all exercises |
| Template update | `{% for exercise in exercises %}` replaces 6 hardcoded cards |
| Add exercise | `POST /workouts/add` creates Exercise in DB |
| Edit/Delete | `POST /workouts/<id>/edit`, `POST /workouts/<id>/delete` |

**Template changes:**
- Replace 6 hardcoded `.exercise-card` divs with a single `{% for %}` loop
- Each card's content (name, difficulty, sets, reps, rest, form instructions) comes from the Exercise model
- Add/Delete buttons change from `alert()` to `<form method="POST">`

### 3C: Goals Page

| Activity | Details |
|----------|---------|
| Route handler | `GET /goals` queries all goals + aggregated stats |
| Template update | `{% for goal in goals %}` replaces 4 hardcoded goal items |
| Add goal | `POST /goals/add` creates Goal in DB |
| Complete/Delete | `POST /goals/<id>/complete`, `POST /goals/<id>/delete` |

**Template changes:**
- Progress stats (completed count, total, percentage) computed server-side
- Goal list items rendered from DB loop
- Gallery section preserved as-is (static for now)
- Modal form `action="/goals/add"` with `method="POST"`

### 3D: Health Page

| Activity | Details |
|----------|---------|
| Route handler | `GET /health` queries latest profile + all records |
| Template update | Stats cards show latest values; health plan items from DB |
| Add record | `POST /health/add` creates HealthRecord |
| Export | `GET /health/export` generates TXT file response |
| BMI calculation | `HealthService.calculate_bmi(weight, height)` |

**Template changes:**
- Form fields populated with latest health record values
- Stats cards (weight, height, body fat) show latest from DB
- Health plan items rendered from DB loop
- Chart data passed as list to template (for JS rendering)

### Exit Criteria
- Dashboard shows live counts from database
- Workouts page lists exercises from DB, add/delete works
- Goals page shows goals from DB, add/complete/delete works
- Health page shows metrics, add record works, export downloads file
- All pages maintain identical visual appearance

---

## Phase 4: Advanced Pages

**Goal:** Convert the remaining 6 pages to dynamic rendering.

**Duration:** ~10 hours

### 4A: Calendar Page

| Activity | Details |
|----------|---------|
| Route handler | `GET /calendar` renders calendar grid + plan list |
| API endpoint | `GET /calendar/api/events` returns JSON for JS calendar rendering |
| JS update | `calendar.js` fetches events from API instead of using hardcoded `workoutPlans` object |
| Add event | `POST /calendar/add` creates CalendarEvent |

**Approach:** The calendar grid is generated client-side by JS (as in the original). The Flask route provides events as JSON. JS fetches and renders.

### 4B: Schedule Page

| Activity | Details |
|----------|---------|
| Route handler | `GET /schedule` queries all schedule items + sticky notes |
| Template update | Weekly schedule days rendered from DB; sticky notes from DB |
| Add schedule | `POST /schedule/add` creates ScheduleItem |
| Sticky notes | `POST /schedule/notes/add`, `POST /schedule/notes/<id>/delete` |

### 4C: Plan Page

| Activity | Details |
|----------|---------|
| Route handler | `GET /plan` queries all plans + aggregated stats |
| Template update | Plan cards rendered from DB; stats computed server-side |
| Timeline | Passed as JSON to JS for rendering |
| Add/Edit/Delete | CRUD routes for Plan model |

### 4D: Tournament Page

| Activity | Details |
|----------|---------|
| Route handler | `GET /tournament` queries UserLevel + all challenges |
| Template update | Level display, stats, challenge list all from DB |
| Join tournament | `POST /tournament/join` (updates user level/stats) |
| Challenge actions | `POST /tournament/challenge/<id>/start` |

### 4E: Motivation Page

| Activity | Details |
|----------|---------|
| Route handler | `GET /motivation` queries all motivation items |
| Template update | Cards rendered from DB; category filtering via query param |
| Add content | `POST /motivation/add` creates Motivation record |
| Favorite/Delete | `POST /motivation/<id>/favorite`, `POST /motivation/<id>/delete` |
| Filtering | `?category=video` query param filters results |

### 4F: Videos Page

| Activity | Details |
|----------|---------|
| Route handler | `GET /videos` queries all videos |
| Template update | Video cards rendered from DB; filtering via query param |
| Upload | `POST /videos/upload` saves file + creates Video record |
| Player | JS reads video data attributes, opens modal (same as original) |
| Social sharing | Preserved as-is (client-side alerts) |

### Exit Criteria
- All 10 pages render from database
- All CRUD operations work via form submissions
- Calendar renders events from DB
- Category filtering works on Motivation and Videos pages
- All modals submit to Flask routes

---

## Phase 5: Form Processing & Validation

**Goal:** Ensure all form submissions are properly handled with validation and error messages.

**Duration:** ~6 hours

### Activities

| # | Activity | Details |
|---|----------|---------|
| 5.1 | Form validation | Add server-side validation for all POST routes (required fields, data types) |
| 5.2 | Flash messages | Implement Flask `flash()` for success/error feedback |
| 5.3 | Error handling | Add 404 and 500 error pages |
| 5.4 | File uploads | Implement proper file upload handling with size limits and type validation |
| 5.5 | Redirect patterns | POST -> Redirect -> GET (PRG pattern) for all form submissions |
| 5.6 | Form repopulation | On validation failure, repopulate form fields with submitted values |

### Flash Message Examples
```python
# In route handler
flash('Exercise added successfully!', 'success')
flash('Please fill in all required fields.', 'error')
return redirect(url_for('workouts.list'))

# In template
{% with messages = get_flashed_messages(with_categories=true) %}
    {% for category, message in messages %}
        <div class="alert alert-{{ category }}">{{ message }}</div>
    {% endfor %}
{% endwith %}
```

### Exit Criteria
- All forms submit successfully
- Validation errors show inline or via flash messages
- File uploads work for Goals (media) and Videos
- Data export works for Health
- No unhandled exceptions on any form submission

---

## Phase 6: Seed Data & Polish

**Goal:** Populate database with prototype data and finalize everything.

**Duration:** ~4 hours

### Activities

| # | Activity | Details |
|---|----------|---------|
| 6.1 | Create `seed.py` | Script that populates all tables with data extracted from the original HTML files |
| 6.2 | Seed exercises | 6 exercises from `Workouts.html` (Push-ups, Pull-ups, Muscle-ups, etc.) |
| 6.3 | Seed goals | 4 goals from `Goals.html` (100 Push-ups, Muscle-up, Handstand, Planche) |
| 6.4 | Seed plans | 5 plans from `Plan.html` |
| 6.5 | Seed schedule | Weekly schedule items from `Schedule.html` |
| 6.6 | Seed calendar | Calendar events from `calander.html` JS data |
| 6.7 | Seed health | Health records from `Health.html` JS data |
| 6.8 | Seed tournament | Level data + 4 challenges from `Tournament.html` |
| 6.9 | Seed videos | 6 videos from `videos.html` |
| 6.10 | Seed motivation | 8 items from `Motivation.html` |
| 6.11 | Seed sticky notes | 4 notes from `Schedule.html` |
| 6.12 | Final visual test | Compare every page side-by-side with original HTML files |
| 6.13 | README update | Update README.md with new Flask setup instructions |

### Seed Data Volume

| Model | Count | Source File |
|-------|-------|-------------|
| Exercise | 6 | Workouts.html |
| Goal | 4 | Goals.html |
| Plan | 5 | Plan.html |
| ScheduleItem | ~12 | Schedule.html |
| CalendarEvent | ~12 | calander.html (from JS `workoutPlans`) |
| HealthRecord | 5 | Health.html (from JS `healthRecords`) |
| HealthPlanItem | 4 | Health.html |
| TournamentChallenge | 4 | Tournament.html |
| UserLevel | 1 | Tournament.html |
| Video | 6 | videos.html |
| Motivation | 8 | Motivation.html |
| StickyNote | 4 | Schedule.html |

### Exit Criteria
- `python seed.py` populates all tables
- Every page shows data matching the original HTML prototypes
- README has clear setup instructions
- No visual differences between dynamic and static versions

---

## Phase Dependencies

```
Phase 1 (Foundation)
    │
    ├──> Phase 2 (CSS/JS Extraction) ──> Phase 3 (Core Pages)
    │                                        │
    │                                        ├──> Phase 4 (Advanced Pages)
    │                                        │        │
    │                                        │        ├──> Phase 5 (Forms)
    │                                        │        │        │
    │                                        │        │        └──> Phase 6 (Seed & Polish)
    │                                        │        │
    │                                        └───────┘
    │
    └──> Phase 2 can start after Phase 1 base.html is ready
```

---

## Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| CSS extraction breaks layout | High | Extract incrementally, test after each file |
| JS breaks after extraction | High | Test each JS file in isolation before removing inline scripts |
| Data model mismatches | Medium | Use seed.py to validate all data fits models |
| Calendar JS rendering | Medium | Keep client-side rendering, only change data source |
| File upload security | Medium | Validate file types, size limits, use secure filenames |
| Template syntax errors | Low | Use Jinja2 linting, test each template individually |
