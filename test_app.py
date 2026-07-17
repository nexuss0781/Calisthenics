"""Single comprehensive test for the Calisthenics Flask app."""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from app import create_app, db


def test_app():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        routes = {
            '/': 200,
            '/workouts/': 200,
            '/goals/': 200,
            '/calendar/': 200,
            '/schedule/': 200,
            '/health/': 200,
            '/plan/': 200,
            '/tournament/': 200,
            '/motivation/': 200,
            '/videos/': 200,
        }

        print("=" * 50)
        print("Calisthenics Flask App - Full Test")
        print("=" * 50)

        passed = 0
        failed = 0

        # Test 1: Database tables created
        with app.app_context():
            tables = db.engine.table_names() if hasattr(db.engine, 'table_names') else db.inspect(db.engine).get_table_names()
            print(f"\n[1] Database tables created: {tables}")
            assert len(tables) >= 10, f"Expected >=10 tables, got {len(tables)}"
            print("    PASS: All tables exist")
            passed += 1

        # Test 2: All routes return 200
        print("\n[2] Route status codes:")
        for route, expected in routes.items():
            resp = client.get(route)
            status = resp.status_code
            ok = status == expected
            print(f"    {route:20s} -> {status} {'PASS' if ok else 'FAIL'}")
            if ok:
                passed += 1
            else:
                failed += 1

        # Test 3: Sidebar renders on every page
        print("\n[3] Sidebar renders on all pages:")
        sidebar_ok = True
        for route in routes:
            resp = client.get(route)
            html = resp.data.decode()
            if 'class="sidebar"' in html and 'Calisthenics' in html:
                pass
            else:
                print(f"    FAIL: Sidebar missing on {route}")
                sidebar_ok = False
                failed += 1
        if sidebar_ok:
            print("    PASS: Sidebar present on all 10 pages")
            passed += 1

        # Test 4: Active page highlighting
        print("\n[4] Active page highlighting:")
        active_ok = True
        expected_active = {
            '/': 'home',
            '/workouts/': 'workouts',
            '/goals/': 'goals',
            '/calendar/': 'calendar',
            '/schedule/': 'schedule',
            '/health/': 'health',
            '/plan/': 'plan',
            '/tournament/': 'tournament',
            '/motivation/': 'motivation',
            '/videos/': 'videos',
        }
        for route, page in expected_active.items():
            resp = client.get(route)
            html = resp.data.decode()
            if f'data-page="{page}"' in html and 'class="active"' in html:
                pass
            else:
                print(f"    FAIL: Active state wrong on {route}")
                active_ok = False
                failed += 1
        if active_ok:
            print("    PASS: Active state correct on all pages")
            passed += 1

        # Test 5: Static CSS files load
        print("\n[5] Static CSS files:")
        css_files = [
            'css/main.css', 'css/dashboard.css', 'css/workouts.css',
            'css/goals.css', 'css/calendar.css', 'css/schedule.css',
            'css/health.css', 'css/plan.css', 'css/tournament.css',
            'css/motivation.css', 'css/videos.css',
        ]
        css_ok = True
        for css in css_files:
            resp = client.get(f'/static/{css}')
            if resp.status_code != 200:
                print(f"    FAIL: /static/{css} -> {resp.status_code}")
                css_ok = False
                failed += 1
        if css_ok:
            print(f"    PASS: All {len(css_files)} CSS files load")
            passed += 1

        # Test 6: Static JS loads
        print("\n[6] Static JS:")
        resp = client.get('/static/js/main.js')
        js_ok = resp.status_code == 200
        print(f"    /static/js/main.js -> {resp.status_code} {'PASS' if js_ok else 'FAIL'}")
        if js_ok:
            passed += 1
        else:
            failed += 1

        # Test 7: Page content present
        print("\n[7] Key content per page:")
        content_checks = {
            '/': ['Dashboard', 'Total Workouts', 'Goals Achieved', 'Recent Workouts'],
            '/workouts/': ['Workouts', 'Push-ups', 'Pull-ups', 'Muscle-ups', 'Add Exercise'],
            '/goals/': ['Goals', '100 Push-ups in a Row', 'First Muscle-up', 'Planche Progression'],
            '/calendar/': ['Calendar', 'Workout Calendar', 'Plan Overview'],
            '/schedule/': ['Schedule', 'Weekly Schedule', 'Monday', 'Wednesday', 'Form Check'],
            '/health/': ['Health Metrics', 'Basic Information', 'BMI', 'Weight Progress'],
            '/plan/': ['Training Plan', 'Upper Body Strength', 'Core Development', 'Timeline'],
            '/tournament/': ['Tournament', 'Your Level', '27', 'Push-up Endurance'],
            '/motivation/': ['Motivation', 'Calisthenics Mastery', 'The Bodyweight Solution'],
            '/videos/': ['Videos', 'Beginner Push-up Tutorial', 'Pull-up Progression'],
        }
        content_ok = True
        for route, keywords in content_checks.items():
            resp = client.get(route)
            html = resp.data.decode()
            missing = [kw for kw in keywords if kw not in html]
            if missing:
                print(f"    FAIL: {route} missing: {missing}")
                content_ok = False
                failed += 1
        if content_ok:
            print("    PASS: All key content present on all pages")
            passed += 1

        # Test 8: No inline <style> tags in templates
        print("\n[8] No inline <style> tags:")
        style_ok = True
        for route in routes:
            resp = client.get(route)
            html = resp.data.decode()
            if '<style>' in html:
                print(f"    FAIL: Inline <style> found on {route}")
                style_ok = False
                failed += 1
        if style_ok:
            print("    PASS: No inline <style> tags in any template")
            passed += 1

        # Summary
        total = passed + failed
        print("\n" + "=" * 50)
        print(f"Results: {passed}/{total} passed, {failed} failed")
        print("=" * 50)
        return failed == 0


if __name__ == '__main__':
    success = test_app()
    sys.exit(0 if success else 1)
