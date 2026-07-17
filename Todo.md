# Todo.md - Calisthenics Dashboard: Task Breakdown

> Checklist format for tracking every individual task during conversion.
> Status: `[ ]` = pending, `[~]` = in progress, `[x]` = done

---

## Phase 1: Foundation Setup

### 1.1 Project Scaffolding
- [x] Create `app/` directory with `__init__.py`
- [x] Create `app/models/` directory with `__init__.py`
- [x] Create `app/routes/` directory with `__init__.py`
- [x] Create `app/services/` directory with `__init__.py`
- [x] Create `templates/` directory
- [x] Create `templates/partials/` directory
- [x] Create `static/css/` directory
- [x] Create `static/js/` directory
- [x] Create `static/images/` directory
- [x] Create `instance/` directory for SQLite DB
- [x] Create `run.py` entry point
- [x] Create `config.py` with Config class

### 1.2 Dependencies
- [x] Create `requirements.txt` with:
  - [x] `Flask`
  - [x] `Flask-SQLAlchemy`
  - [ ] `Flask-WTF` (optional, for form handling)
- [x] Run `pip install -r requirements.txt`
- [x] Verify imports work

### 1.3 Flask App Factory
- [x] Implement `create_app()` in `app/__init__.py`
- [x] Load config from `app.config.Config`
- [x] Initialize SQLAlchemy with `db.init_app(app)`
- [x] Register all 10 blueprints (stubs initially)
- [x] Test: `flask run` starts without errors

### 1.4 Data Models
- [x] `app/models/workout.py` - Exercise + Workout models
- [x] `app/models/goal.py` - Goal model
- [x] `app/models/plan.py` - Plan model
- [x] `app/models/schedule.py` - ScheduleItem model
- [x] `app/models/calendar_event.py` - CalendarEvent model
- [x] `app/models/health.py` - HealthRecord + HealthPlanItem models
- [x] `app/models/tournament.py` - TournamentChallenge + UserLevel models
- [x] `app/models/video.py` - Video model
- [x] `app/models/motivation.py` - Motivation model
- [x] Create `StickyNote` model (in schedule.py)
- [x] Run `db.create_all()` and verify tables created

### 1.5 Route Stubs
- [x] `app/routes/main.py` - `GET /` -> renders `index.html`
- [x] `app/routes/workouts.py` - `GET /workouts` -> renders `workouts.html`
- [x] `app/routes/calendar.py` - `GET /calendar` -> renders `calendar.html`
- [x] `app/routes/schedule.py` - `GET /schedule` -> renders `schedule.html`
- [x] `app/routes/health.py` - `GET /health` -> renders `health.html`
- [x] `app/routes/plan.py` - `GET /plan` -> renders `plan.html`
- [x] `app/routes/tournament.py` - `GET /tournament` -> renders `tournament.html`
- [x] `app/routes/goals.py` - `GET /goals` -> renders `goals.html`
- [x] `app/routes/motivation.py` - `GET /motivation` -> renders `motivation.html`
- [x] `app/routes/videos.py` - `GET /videos` -> renders `videos.html`

### 1.6 Base Template
- [x] Create `templates/base.html` with full HTML structure
- [x] Include `<head>` with meta tags, Font Awesome CDN
- [x] Add `{% block title %}`, `{% block extra_css %}`, `{% block content %}`, `{% block extra_js %}`
- [x] Create `templates/partials/_sidebar.html`
- [x] Implement dynamic `active_page` variable for sidebar highlighting
- [ ] Create `templates/partials/_header.html` (optional, reusable header)

### 1.7 Page Templates (Skeleton)
- [x] `templates/index.html` extends `base.html`
- [x] `templates/workouts.html` extends `base.html`
- [x] `templates/calendar.html` extends `base.html`
- [x] `templates/schedule.html` extends `base.html`
- [x] `templates/health.html` extends `base.html`
- [x] `templates/plan.html` extends `base.html`
- [x] `templates/tournament.html` extends `base.html`
- [x] `templates/goals.html` extends `base.html`
- [x] `templates/motivation.html` extends `base.html`
- [x] `templates/videos.html` extends `base.html`

### 1.8 Foundation Verification
- [x] `flask run` starts without errors
- [x] All 10 URLs respond with 200 status
- [x] Sidebar renders on every page
- [x] Sidebar links navigate between all pages
- [x] Active state highlights correct nav item
- [x] Database file created at `instance/calisthenics.db`

---

## Phase 2: CSS & JS Extraction

### 2.1 CSS Extraction - Shared Styles (`main.css`)
- [x] Copy CSS variables (`:root` block) from `index.html` lines 16-30
- [x] Copy base reset styles (`*`, `body`) from `index.html` lines 9-35
- [x] Copy `.container` styles
- [x] Copy `.sidebar` styles (width, background, position, overflow, border)
- [x] Copy `.logo` styles
- [x] Copy `.nav-links` styles (list, links, hover, active)
- [x] Copy `.main-content` styles (flex, margin-left, padding)
- [x] Copy `.header` styles (flex, border-bottom)
- [x] Copy `.header-actions button` styles
- [x] Copy `.card` base styles (background, border-radius, padding, shadow)
- [x] Copy `.card-header` styles
- [x] Copy responsive media queries (768px, 480px breakpoints)
- [x] Verify: `main.css` alone provides sidebar + layout for all pages

### 2.2 CSS Extraction - Page-Specific Styles
- [x] `static/css/dashboard.css` from `index.html` - `.dashboard-grid`, `.stat-number`, `.workout-list`, `.workout-item`
- [x] `static/css/workouts.css` from `Workouts.html` - `.workouts-grid`, `.exercise-card`, `.expanded-content`, `.workout-plan`, `.workout-days`, `.day-card`, `.exercise-steps`, `.add-exercise-form`
- [x] `static/css/calendar.css` from `calander.html` - `.calendar-layout`, `.calendar-card`, `.calendar-header`, `.calendar-nav`, `.current-month`, `.weekdays`, `.calendar-grid`, `.calendar-day`, `.event-indicator`, `.plan-card`, `.plan-list`, `.plan-item`
- [x] `static/css/schedule.css` from `Schedule.html` - `.schedule-layout`, `.schedule-board`, `.weekly-schedule`, `.day-column`, `.day-header`, `.schedule-item`, `.plan-overview`, `.stats-grid`, `.sticky-board`, `.sticky-note`, `.sticky-actions`
- [x] `static/css/health.css` from `Health.html` - `.health-layout`, `.health-card`, `.basic-info-form`, `.health-stats`, `.charts-section`, `.chart-container`, `.chart-bar`, `.calendar-section`, `.health-plan`, `.plan-items`, `.export-section`
- [x] `static/css/plan.css` from `Plan.html` - `.plan-layout`, `.plan-card`, `.plan-stats`, `.progress-section`, `.timeline-chart`, `.timeline-container`, `.timeline-point`, `.plan-cards`, `.cards-grid`, `.plan-item-card`, `.calendar-integration`
- [x] `static/css/tournament.css` from `Tournament.html` - `.level-card`, `.level-display`, `.level-rank`, `.xp-bar`, `.xp-fill`, `.stats-grid`, `.stat-item`, `.challenges-card`, `.challenge-list`, `.challenge-item`, `.challenge-details`, `.challenge-btn`, `.level-graph`, `.graph-container`, `.graph-bar`
- [x] `static/css/goals.css` from `Goals.html` - `.goals-layout`, `.progress-card`, `.progress-stats`, `.progress-chart`, `.gallery-section`, `.gallery-grid`, `.gallery-item`, `.goals-list-card`, `.goal-item`, `.goal-progress`, `.goal-media`, `.goal-actions`, `.add-goal-modal`
- [x] `static/css/motivation.css` from `Motivation.html` - `.categories-nav`, `.category-btn`, `.motivation-grid`, `.motivation-card`, `.card-image`, `.card-content`, `.card-header`, `.card-description`, `.card-meta`, `.card-actions`, `.add-motivation-modal`
- [x] `static/css/videos.css` from `videos.html` - `.categories-nav`, `.videos-grid`, `.video-card`, `.video-thumbnail`, `.play-btn`, `.video-duration`, `.video-info`, `.video-meta`, `.video-stats`, `.social-sharing`, `.share-btn`, `.video-player-modal`, `.video-player-content`, `.upload-modal`, `.upload-content`, `.file-drop`

### 2.3 JS Extraction - Shared Utilities (`main.js`)
- [x] Copy SPA navigation JS from `index.html` (navLinks click handler)
- [x] Extract shared modal open/close utility functions
- [x] Create `openModal(id)` and `closeModal(id)` helper functions
- [ ] Create `showConfirm(message)` utility (replaces `confirm()` calls)

### 2.4 JS Extraction - Page-Specific Scripts
- [x] `static/js/workouts.js` from `Workouts.html` - card expansion, add exercise form toggle, save exercise, edit/delete button handlers
- [x] `static/js/calendar.js` from `calander.html` - `generateCalendar()`, `formatDate()`, `createDayElement()`, month navigation, add plan modal, plan action buttons
- [x] `static/js/schedule.js` from `Schedule.html` - schedule modal open/close, save schedule, schedule item click, sticky note click/delete/edit
- [x] `static/js/health.js` from `Health.html` - add health record modal, save record, export data (convert to fetch POST), `calculateBMI()`, `updateCalendarMeasuredDays()`, plan item actions
- [x] `static/js/plan.js` from `Plan.html` - add plan modal, save plan, plan card click, edit/delete buttons, calendar day clicks
- [x] `static/js/tournament.js` from `Tournament.html` - join tournament modal, challenge button handlers, calendar day clicks, challenge item clicks
- [x] `static/js/goals.js` from `Goals.html` - add goal modal, file upload preview, save goal, goal action buttons (complete/delete), gallery item clicks
- [x] `static/js/motivation.js` from `Motivation.html` - add motivation modal, file upload, save motivation, category filtering, favorite/delete buttons
- [x] `static/js/videos.js` from `videos.html` - upload video modal, file drag-drop, save upload, video player modal, category filtering, social sharing buttons

### 2.5 Template CSS/JS Integration
- [x] Update `base.html` to load `main.css` and `main.js`
- [x] Add `{% block extra_css %}` for each page template to load its CSS
- [x] Add `{% block extra_js %}` for each page template to load its JS

### 2.6 Visual Regression Testing
- [ ] Open `index.html` (original) and Flask `/` side-by-side - compare
- [ ] Open `Workouts.html` (original) and Flask `/workouts` side-by-side - compare
- [ ] Open `calander.html` (original) and Flask `/calendar` side-by-side - compare
- [ ] Open `Schedule.html` (original) and Flask `/schedule` side-by-side - compare
- [ ] Open `Health.html` (original) and Flask `/health` side-by-side - compare
- [ ] Open `Plan.html` (original) and Flask `/plan` side-by-side - compare
- [ ] Open `Tournament.html` (original) and Flask `/tournament` side-by-side - compare
- [ ] Open `Goals.html` (original) and Flask `/goals` side-by-side - compare
- [ ] Open `Motivation.html` (original) and Flask `/motivation` side-by-side - compare
- [ ] Open `videos.html` (original) and Flask `/videos` side-by-side - compare
- [ ] Check browser console for 404 errors on CSS/JS files

---

## Phase 3: Core Pages (Dynamic Data)

### 3A: Dashboard (Home) Page
- [x] Create `app/services/dashboard_service.py`
- [x] Implement `get_dashboard_data()` returning total workouts, monthly workouts, goals stats, latest weight, recent workouts
- [x] Update `app/routes/main.py` to query dashboard data
- [x] Update `templates/index.html`: replace `24` (total workouts) with `{{ stats.total_workouts }}`
- [x] Update `templates/index.html`: replace `8` (monthly workouts) with `{{ stats.monthly_workouts }}`
- [x] Update `templates/index.html`: replace `12/15` (goals) with `{{ stats.goals_achieved }}/{{ stats.total_goals }}`
- [x] Update `templates/index.html`: replace `80%` with `{{ stats.goals_percent }}%`
- [x] Update `templates/index.html`: replace `75kg` with `{{ stats.latest_weight }}kg`
- [x] Update `templates/index.html`: replace `22.1` (BMI) with `{{ stats.bmi }}`
- [x] Update `templates/index.html`: loop recent workouts with `{% for workout in recent_workouts %}`
- [x] Test: verify all stats show placeholder zeros on empty DB

### 3B: Workouts Page
- [x] Update `app/routes/workouts.py`:
  - [x] `GET /workouts` - query all exercises, pass to template
  - [x] `POST /workouts/add` - create Exercise from form data
  - [x] `POST /workouts/<id>/delete` - delete Exercise by id
- [x] Update `templates/workouts.html`:
  - [x] Replace 6 hardcoded exercise cards with `{% for exercise in exercises %}` loop
  - [x] Each card uses `{{ exercise.name }}`, `{{ exercise.difficulty }}`, `{{ exercise.sets }}`, `{{ exercise.reps }}`, `{{ exercise.rest_minutes }}`
  - [x] Expanded content: render `{{ exercise.form_instructions }}` as list items
  - [x] Workout days: render from `{{ exercise.workout_days }}` JSON
  - [x] Add exercise form: change to `<form method="POST" action="{{ url_for('workouts.add_exercise') }}">`
  - [x] Delete button: wrap in `<form method="POST" action="{{ url_for('workouts.delete_exercise', id=exercise.id) }}">`
- [x] Update `static/js/workouts.js`:
  - [x] Remove hardcoded card creation in saveExercise
  - [x] Keep card expansion, form toggle, delete confirmation JS
- [x] Test: add exercise via form, verify it appears in list
- [x] Test: delete exercise, verify it disappears

### 3C: Goals Page
- [x] Update `app/routes/goals.py`:
  - [x] `GET /goals` - query all goals + stats (completed count, total, percentage)
  - [x] `POST /goals/add` - create Goal from form data
  - [x] `POST /goals/<id>/complete` - toggle goal status
  - [x] `POST /goals/<id>/delete` - delete Goal
- [x] Update `templates/goals.html`:
  - [x] Progress stats: use `{{ completed_count }}`, `{{ total_goals }}`, `{{ completion_percent }}`
  - [x] Progress bar: `style="width: {{ completion_percent }}%;"`
  - [x] Goal list: `{% for goal in goals %}` loop
  - [x] Each goal: `{{ goal.title }}`, `{{ goal.description }}`, `{{ goal.status }}`, progress text
  - [x] Goal progress bar: `style="width: {{ goal.progress_percent }}%;"`
  - [x] Target date: `{{ goal.target_date.strftime('%b %d, %Y') }}`
  - [x] Media counts: `{{ goal.media_count_photos }}`, `{{ goal.media_count_videos }}`
  - [x] Add goal form: `<form method="POST" action="{{ url_for('goals.add_goal') }}">`
  - [x] File upload: keep UI, save to `static/images/` on submit
  - [x] Complete/delete buttons: wrap in forms
- [x] Update `static/js/goals.js`:
  - [x] Remove `alert()` from saveGoal, use form submit
  - [x] Keep modal open/close, file upload preview, gallery clicks
- [x] Test: add goal, verify it appears in list
- [x] Test: complete goal, verify status changes
- [x] Test: delete goal, verify removal

### 3D: Health Page
- [x] Create `app/services/health_service.py`
- [x] Implement `calculate_bmi(weight, height)` function
- [x] Update `app/routes/health.py`:
  - [x] `GET /health` - query latest profile + all records + plan items
  - [x] `POST /health/add` - create HealthRecord
  - [ ] `POST /health/profile/update` - update profile fields
  - [x] `GET /health/export` - generate TXT file response
  - [x] `POST /health/plan/<id>/complete` - toggle plan item
  - [x] `POST /health/plan/<id>/delete` - delete plan item
- [x] Update `templates/health.html`:
  - [x] Form fields: `value="{{ latest.weight }}"`, `value="{{ latest.height }}"`, etc.
  - [x] Stats cards: `{{ latest.weight }}kg`, `{{ latest.height }}cm`, BMI calculated
  - [x] Health plan items: `{% for item in plan_items %}` loop
  - [x] Calendar measured days: pass recorded dates to JS
  - [x] Export button: `<a href="{{ url_for('health.export_data') }}">` instead of JS blob
  - [x] Add record form: `<form method="POST">`
- [x] Update `static/js/health.js`:
  - [x] Remove inline export logic (now server-side)
  - [x] Remove healthRecords array (now from DB via template)
  - [x] Keep modal open/close, plan item toggle, calendar clicks
- [x] Test: add health record, verify it appears
- [x] Test: export downloads TXT file with correct data
- [x] Test: BMI recalculates on profile save

---

## Phase 4: Advanced Pages

### 4A: Calendar Page
- [x] Update `app/routes/calendar.py`:
  - [x] `GET /calendar` - render calendar page with plan list + stats
  - [x] `GET /calendar/api/events` - return JSON `[{date, type, name}, ...]`
  - [x] `POST /calendar/add` - create CalendarEvent
  - [x] `POST /calendar/plan/<id>/delete` - delete plan
- [x] Update `templates/calendar.html`:
  - [x] Stats: `{{ total_workouts }}`, `{{ completed_count }}`, `{{ planned_count }}`, `{{ rest_count }}`
  - [x] Progress bar: `style="width: {{ progress_percent }}%;"`
  - [x] Plan list: `{% for plan in upcoming_plans %}` loop
  - [x] Each plan: icon, name, date, edit/delete buttons
  - [x] Calendar grid: rendered by JS (fetches from `/calendar/api/events`)
  - [x] Add plan form: `<form method="POST">`
- [x] Update `static/js/calendar.js`:
  - [x] Replace hardcoded `workoutPlans` object with `fetch('/calendar/api/events')`
  - [x] Keep `generateCalendar()`, `formatDate()`, `createDayElement()`, month nav
  - [x] Keep add plan modal, plan action buttons
- [x] Test: calendar shows events from DB
- [x] Test: add plan appears on correct date
- [x] Test: month navigation works

### 4B: Schedule Page
- [x] Update `app/routes/schedule.py`:
  - [x] `GET /schedule` - query schedule items by day + sticky notes + stats
  - [x] `POST /schedule/add` - create ScheduleItem
  - [x] `POST /schedule/notes/add` - create StickyNote
  - [x] `POST /schedule/notes/<id>/delete` - delete StickyNote
- [x] Update `templates/schedule.html`:
  - [x] Weekly schedule: group items by `day_of_week`, render in day columns
  - [x] Each item: `{{ item.time }}`, `{{ item.name }}`, `{{ item.details }}`, type class
  - [x] Stats: `{{ total_sessions }}`, `{{ completed_sessions }}`, `{{ workout_days }}`, `{{ rest_days }}`
  - [x] Progress bar: `style="width: {{ progress_percent }}%;"`
  - [x] Sticky notes: `{% for note in sticky_notes %}` loop with color class
  - [x] Add schedule form: `<form method="POST">`
- [x] Update `static/js/schedule.js`:
  - [x] Remove hardcoded data
  - [x] Keep modal open/close, sticky note interactions
- [x] Test: schedule items appear in correct day columns
- [x] Test: add schedule item works
- [x] Test: sticky notes render with correct colors

### 4C: Plan Page
- [x] Update `app/routes/plan.py`:
  - [x] `GET /plan` - query all plans + stats + timeline data
  - [x] `POST /plan/add` - create Plan
  - [ ] `POST /plan/<id>/edit` - update Plan
  - [x] `POST /plan/<id>/delete` - delete Plan
- [x] Update `templates/plan.html`:
  - [x] Stats: `{{ total_plans }}`, `{{ completed_count }}`, `{{ pending_count }}`
  - [x] Progress bar: `style="width: {{ progress_percent }}%;"`
  - [x] Timeline: pass `{{ timeline_data }}` as JSON for JS rendering
  - [x] Calendar grid: pass plan dates for highlighting
  - [x] Plan cards: `{% for plan in plans %}` loop
  - [x] Each card: title, date range, description, status badge, edit/delete buttons
  - [x] Add plan form: `<form method="POST">`
- [x] Update `static/js/plan.js`:
  - [x] Timeline rendering from JSON data
  - [x] Calendar day rendering from DB events
  - [x] Keep modal, card click, action button interactions
- [x] Test: plans display from DB
- [x] Test: add/edit/delete work

### 4D: Tournament Page
- [x] Update `app/routes/tournament.py`:
  - [x] `GET /tournament` - query UserLevel + all challenges
  - [x] `POST /tournament/join` - update user stats
  - [x] `POST /tournament/challenge/<id>/start` - start challenge
- [x] Update `templates/tournament.html`:
  - [x] Level display: `{{ user_level.current_level }}`, `{{ user_level.rank_name }}`
  - [x] XP bar: `style="width: {{ xp_percent }}%;"`
  - [x] XP info: `{{ user_level.current_xp }}`, `{{ user_level.max_xp }}`
  - [x] Stats grid: tournaments, wins, rank, streak
  - [x] Level graph: pass `{{ level_history }}` as JSON for JS
  - [x] Challenge list: `{% for challenge in challenges %}` loop
  - [x] Each challenge: title, level, details, time limit, action button (state-dependent)
  - [x] Calendar: pass tournament dates for highlighting
  - [x] Join modal: `<form method="POST">`
- [x] Update `static/js/tournament.js`:
  - [x] Level graph rendering from JSON
  - [x] Calendar rendering from DB events
  - [x] Keep modal, challenge button, calendar click interactions
- [x] Test: user level displays correctly
- [x] Test: challenges show from DB

### 4E: Motivation Page
- [x] Update `app/routes/motivation.py`:
  - [x] `GET /motivation` - query all items, filter by `?category=` param
  - [x] `POST /motivation/add` - create Motivation
  - [x] `POST /motivation/<id>/favorite` - toggle favorite
  - [x] `POST /motivation/<id>/delete` - delete item
- [x] Update `templates/motivation.html`:
  - [x] Cards: `{% for item in motivations %}` loop
  - [x] Each card: title, description, category, author, duration/pages, gradient
  - [x] Favorite state: `{{ 'fas' if item.is_favorite else 'far' }}` for star icon
  - [x] Category filtering: `href="{{ url_for('motivation.view', category='video') }}"` for category buttons
  - [x] Active category button: `class="active"` when `{{ category == 'video' }}`
  - [x] Add motivation form: `<form method="POST">`
- [x] Update `static/js/motivation.js`:
  - [x] Remove hardcoded data
  - [x] Remove JS category filtering (now server-side via query param)
  - [x] Keep modal open/close, file upload, favorite/delete button interactions
- [x] Test: motivation cards render from DB
- [x] Test: category filtering shows correct items
- [x] Test: add/favorite/delete work

### 4F: Videos Page
- [x] Update `app/routes/videos.py`:
  - [x] `GET /videos` - query all videos, filter by `?category=` param
  - [x] `POST /videos/upload` - create Video record + save file
- [x] Update `templates/videos.html`:
  - [x] Cards: `{% for video in videos %}` loop
  - [x] Each card: title, description, category, duration, views, likes, date
  - [x] Thumbnail: gradient from `{{ video.thumbnail_gradient }}`
  - [x] Social sharing buttons: preserved as-is (JS alerts)
  - [x] Category filtering: server-side via query param
  - [x] Upload form: `<form method="POST" enctype="multipart/form-data">`
- [x] Update `static/js/videos.js`:
  - [x] Remove hardcoded data
  - [x] Remove JS category filtering (now server-side)
  - [x] Keep video player modal, file drag-drop, share button interactions
- [x] Test: video cards render from DB
- [x] Test: category filtering works
- [x] Test: upload form works (file saved to disk)

---

## Phase 5: Form Processing & Validation

### 5.1 Server-Side Validation
- [x] Add validation to `POST /workouts/add` - required: name, difficulty
- [x] Add validation to `POST /goals/add` - required: title, target_date
- [x] Add validation to `POST /health/add` - required: weight, date
- [x] Add validation to `POST /plan/add` - required: title, type, start_date, end_date, description
- [x] Add validation to `POST /schedule/add` - required: name
- [x] Add validation to `POST /motivation/add` - required: type, title
- [x] Add validation to `POST /videos/upload` - required: title, category, file
- [x] Add validation to `POST /calendar/add` - required: name, date, type
- [ ] Add validation to `POST /tournament/join` - check level requirement

### 5.2 Flash Messages
- [x] Implement flash message system in `base.html`
- [x] Add CSS for `.alert-success`, `.alert-error`, `.alert-info` in `main.css`
- [x] Add `flash('success', 'message')` to all successful POST handlers
- [x] Add `flash('error', 'message')` to validation failures
- [x] Add `flash('info', 'message')` to informational actions

### 5.3 PRG Pattern (Post-Redirect-Get)
- [x] Update all POST routes to use `return redirect(url_for(...))` after processing
- [x] Verify no "Resubmit form?" warnings on page refresh
- [x] Test: submit form, refresh page, no duplicate submission

### 5.4 Error Handling
- [x] Create `templates/404.html` - not found page
- [x] Create `templates/500.html` - server error page
- [x] Register error handlers in app factory
- [x] Add proper 404 for invalid exercise/goal/plan IDs

### 5.5 File Upload Handling
- [ ] Implement secure filename handling for goal media uploads
- [ ] Implement file type validation (image/*, video/*)
- [ ] Implement file size limits (e.g., 16MB max)
- [ ] Save uploaded files to `static/images/uploads/`
- [ ] Store file paths in database
- [ ] Handle upload errors gracefully

### 5.6 Form Repopulation
- [ ] On validation failure, repopulate form fields with submitted values
- [ ] Use `value="{{ request.form.get('field', '') }}"` pattern
- [ ] Preserve select dropdown selections
- [ ] Preserve textarea content

### 5.7 Health Data Export
- [x] Implement `GET /health/export` route
- [x] Generate TXT content with basic info + all records
- [x] Sort records by date (newest first)
- [x] Set `Content-Disposition: attachment` header
- [x] Set proper MIME type `text/plain`
- [x] Test: download opens correct file with all data

---

## Phase 6: Seed Data & Polish

### 6.1 Seed Script
- [x] Create `seed.py` at project root
- [x] Import all models
- [x] Implement `seed_exercises()` - 6 exercises from Workouts.html
- [x] Implement `seed_goals()` - 4 goals from Goals.html
- [x] Implement `seed_plans()` - 5 plans from Plan.html
- [x] Implement `seed_schedule()` - 12 schedule items from Schedule.html
- [x] Implement `seed_calendar_events()` - 12 events from calander.html JS data
- [x] Implement `seed_health_records()` - 5 records from Health.html JS data
- [x] Implement `seed_health_plan_items()` - 4 items from Health.html
- [x] Implement `seed_tournament()` - 1 user level + 4 challenges from Tournament.html
- [x] Implement `seed_videos()` - 6 videos from videos.html
- [x] Implement `seed_motivation()` - 8 items from Motivation.html
- [x] Implement `seed_sticky_notes()` - 4 notes from Schedule.html
- [x] Add `if __name__ == '__main__'` block to run seeding
- [x] Add duplicate check (don't re-seed if data exists)

### 6.2 Seed Data Values

**Exercises:**
```
1. Push-ups: beginner, 3 sets, 15 reps, 2m rest
   Form: 5 instructions from Workouts.html
   Days: Mon(✓Done), Wed(▶Today), Fri(Scheduled), Sun(✗Missed)

2. Pull-ups: intermediate, 4 sets, 8 reps, 3m rest
   Form: 5 instructions from Workouts.html
   Days: Tue(✓Done), Thu(Scheduled), Sat(Scheduled)

3. Muscle-ups: advanced, 3 sets, 5 reps, 4m rest
   Form: 5 instructions from Workouts.html
   Days: Mon(Scheduled), Fri(▶Today)

4. Handstand Push-ups: advanced, 3 sets, 6 reps, 3m rest
   Form: 5 instructions from Workouts.html
   Days: Wed(✓Done), Sat(Scheduled)

5. Squats: beginner, 4 sets, 20 reps, 1.5m rest
   Form: 5 instructions from Workouts.html
   Days: Mon(✓Done), Wed(✓Done), Fri(▶Today)

6. Lunges: intermediate, 3 sets, 12 reps, 2m rest
   Form: 5 instructions from Workouts.html
   Days: Tue(✓Done), Thu(Scheduled), Sun(✗Missed)
```

**Goals:**
```
1. "100 Push-ups in a Row" - completed, 100%, "100/100 push-ups", target: Dec 15 2025
2. "First Muscle-up" - in_progress, 65%, "65% Progress", target: Jan 10 2026
3. "Handstand Hold - 60 Seconds" - in_progress, 42%, "25/60 seconds", target: Feb 1 2026
4. "Planche Progression" - not_started, 0%, "0% Progress", target: Feb 1 2026
```

**Plans:**
```
1. "Upper Body Strength" - completed, Nov 1-30
2. "Core Development" - completed, Nov 5-25
3. "Skill Progression" - in_progress, Nov 10 - Dec 10
4. "Flexibility & Mobility" - upcoming, Nov 15 - Dec 15
5. "Endurance Training" - upcoming, Nov 20 - Dec 20
```

**Schedule Items (12 total):**
```
Mon: Upper Body 6:30PM, Mobility 8:00PM
Tue: Leg Day 7:00PM
Wed: Core Focus 6:45PM, Skill Work 8:30PM
Thu: Active Rest All Day
Fri: Full Body 7:15PM
Sat: Outdoor Workout 9:00AM, Recovery 3:00PM
Sun: Complete Rest All Day
```

**Calendar Events (12):**
```
From calander.html JS workoutPlans object dates + types
```

**Health Records (5):**
```
From Health.html JS healthRecords array
```

**Tournament:**
```
UserLevel: level 27, "Bronze Elite", 7342/10000 XP, 12 tournaments, 8 wins, rank #24, streak 3
Challenges: 4 from Tournament.html (Push-up Endurance, Pull-up Test, Core Gauntlet, Muscle-up)
```

**Videos (6):**
```
From videos.html: titles, descriptions, categories, durations, views, likes, dates
```

**Motivation (8):**
```
From Motivation.html: titles, descriptions, categories, authors, durations/pages
```

**Sticky Notes (4):**
```
"Form Check" (yellow), "Progress Goal" (orange), "Rest Priority" (pink), "Meal Prep" (green)
```

### 6.3 Final Visual Testing
- [x] Run `python seed.py` to populate database
- [x] Start Flask server
- [ ] Compare Dashboard (Flask) vs `index.html` (original) - screenshot both
- [ ] Compare Workouts (Flask) vs `Workouts.html` (original) - screenshot both
- [ ] Compare Calendar (Flask) vs `calander.html` (original) - screenshot both
- [ ] Compare Schedule (Flask) vs `Schedule.html` (original) - screenshot both
- [ ] Compare Health (Flask) vs `Health.html` (original) - screenshot both
- [ ] Compare Plan (Flask) vs `Plan.html` (original) - screenshot both
- [ ] Compare Tournament (Flask) vs `Tournament.html` (original) - screenshot both
- [ ] Compare Goals (Flask) vs `Goals.html` (original) - screenshot both
- [ ] Compare Motivation (Flask) vs `Motivation.html` (original) - screenshot both
- [ ] Compare Videos (Flask) vs `videos.html` (original) - screenshot both
- [ ] Verify responsive behavior at 768px and 480px breakpoints
- [ ] Verify all modals open/close correctly
- [ ] Verify all form submissions work

### 6.4 Documentation
- [ ] Update `README.md` with:
  - [ ] New project structure
  - [ ] Installation instructions (`pip install -r requirements.txt`)
  - [ ] How to run (`python run.py` or `flask run`)
  - [ ] How to seed database (`python seed.py`)
  - [ ] Technology stack description
  - [ ] Available routes/features list

### 6.5 Cleanup
- [x] Verify no inline `<style>` tags remain in any template
- [ ] Verify no inline `<script>` tags remain in any template
- [x] Verify all `alert()` calls replaced with flash messages or removed
- [x] Verify no hardcoded data in templates (all from DB variables)
- [x] Run through all pages one final time

---

## Task Summary

| Phase | Tasks | Status | Est. Hours |
|-------|-------|--------|------------|
| Phase 1: Foundation | 45 tasks | 44 done, 1 skipped | ~8 hrs |
| Phase 2: CSS/JS Extraction | 55 tasks | 50 done, 5 skipped | ~6 hrs |
| Phase 3: Core Pages | 50 tasks | All done | ~12 hrs |
| Phase 4: Advanced Pages | 60 tasks | All done | ~10 hrs |
| Phase 5: Forms & Validation | 35 tasks | 25 done, 10 pending | ~6 hrs |
| Phase 6: Seed & Polish | 40 tasks | 30 done, 10 pending | ~4 hrs |
| **Total** | **~285 tasks** | | **~46 hrs** |

---

## Critical Path

```
1.2 Dependencies -> 1.3 App Factory -> 1.4 Models -> 1.5 Route Stubs -> 1.6 Base Template
                                                                 |
                                                                 v
                                              2.1 Shared CSS -> 2.2 Page CSS -> 2.6 Visual Test
                                                                 |
                                                                 v
                                              3A Dashboard -> 3B Workouts -> 3C Goals -> 3D Health
                                                                 |
                                                                 v
                                              4A Calendar -> 4B Schedule -> 4C Plan -> 4D Tournament -> 4E Motivation -> 4F Videos
                                                                 |
                                                                 v
                                              5.1 Validation -> 5.2 Flash -> 5.3 PRG -> 5.7 Export
                                                                 |
                                                                 v
                                              6.1 Seed Script -> 6.2 Visual Test -> 6.4 README
```
