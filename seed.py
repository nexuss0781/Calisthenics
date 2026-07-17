import json
from datetime import datetime, date
from app import create_app, db
from app.models.workout import Exercise, Workout
from app.models.goal import Goal
from app.models.plan import Plan
from app.models.schedule import ScheduleItem, StickyNote
from app.models.calendar_event import CalendarEvent
from app.models.health import HealthRecord, HealthPlanItem
from app.models.tournament import TournamentChallenge, UserLevel
from app.models.video import Video
from app.models.motivation import Motivation


def seed_database():
    app = create_app()
    with app.app_context():
        if Exercise.query.first() or Workout.query.first():
            print("Database already contains data. Dropping and re-creating tables...")
        else:
            print("Empty database detected. Creating tables...")

        db.drop_all()
        db.create_all()

        print("Seeding Exercises...")
        exercises = [
            Exercise(
                name="Push-ups",
                difficulty="beginner",
                sets=3,
                reps=15,
                rest_minutes=2,
                form_instructions=json.dumps([
                    "Start in a plank position with hands shoulder-width apart",
                    "Lower your body until your chest nearly touches the floor",
                    "Push back up to the starting position",
                    "Keep your core engaged throughout",
                    "Exhale as you push up"
                ]),
                workout_days=json.dumps([
                    {"day": "Mon", "status": "done"},
                    {"day": "Wed", "status": "done"},
                    {"day": "Fri", "status": "today"},
                    {"day": "Sun", "status": "missed"}
                ])
            ),
            Exercise(
                name="Pull-ups",
                difficulty="intermediate",
                sets=4,
                reps=8,
                rest_minutes=3,
                form_instructions=json.dumps([
                    "Grab the bar with an overhand grip slightly wider than shoulders",
                    "Hang with arms fully extended",
                    "Pull yourself up until chin clears the bar",
                    "Lower back down with control",
                    "Avoid swinging or kipping"
                ]),
                workout_days=json.dumps([
                    {"day": "Tue", "status": "done"},
                    {"day": "Thu", "status": "scheduled"},
                    {"day": "Sat", "status": "scheduled"}
                ])
            ),
            Exercise(
                name="Muscle-ups",
                difficulty="advanced",
                sets=3,
                reps=5,
                rest_minutes=4,
                form_instructions=json.dumps([
                    "Start with a false grip on the rings",
                    "Pull yourself up explosively",
                    "Transition your chest over the rings",
                    "Push up to a dip position",
                    "Lower back down with control"
                ]),
                workout_days=json.dumps([
                    {"day": "Mon", "status": "scheduled"},
                    {"day": "Fri", "status": "today"}
                ])
            ),
            Exercise(
                name="Handstand Push-ups",
                difficulty="advanced",
                sets=3,
                reps=6,
                rest_minutes=3,
                form_instructions=json.dumps([
                    "Kick up into a handstand against the wall",
                    "Lower yourself until head nearly touches the floor",
                    "Push back up to full extension",
                    "Keep your body tight and straight",
                    "Breathe out as you push up"
                ]),
                workout_days=json.dumps([
                    {"day": "Wed", "status": "done"},
                    {"day": "Sat", "status": "scheduled"}
                ])
            ),
            Exercise(
                name="Squats",
                difficulty="beginner",
                sets=4,
                reps=20,
                rest_minutes=1.5,
                form_instructions=json.dumps([
                    "Stand with feet shoulder-width apart",
                    "Lower your hips back and down like sitting in a chair",
                    "Keep your chest up and knees over toes",
                    "Drive through your heels to stand up",
                    "Go to at least parallel depth"
                ]),
                workout_days=json.dumps([
                    {"day": "Mon", "status": "done"},
                    {"day": "Wed", "status": "done"},
                    {"day": "Fri", "status": "today"}
                ])
            ),
            Exercise(
                name="Lunges",
                difficulty="intermediate",
                sets=3,
                reps=12,
                rest_minutes=2,
                form_instructions=json.dumps([
                    "Stand tall with feet hip-width apart",
                    "Step forward with one leg into a lunge",
                    "Lower until both knees are at 90 degrees",
                    "Push back to starting position",
                    "Alternate legs each rep"
                ]),
                workout_days=json.dumps([
                    {"day": "Tue", "status": "done"},
                    {"day": "Thu", "status": "scheduled"},
                    {"day": "Sun", "status": "missed"}
                ])
            )
        ]
        db.session.add_all(exercises)
        db.session.commit()
        print(f"  Seeded {len(exercises)} exercises")

        print("Seeding Workouts...")
        workouts = [
            Workout(
                name="Upper Body Blast",
                exercises_used="Push-ups, Pull-ups, Dips",
                scheduled_date=datetime(2025, 11, 8, 18, 30),
                completed=True
            ),
            Workout(
                name="Leg Day",
                exercises_used="Squats, Lunges, Calf Raises",
                scheduled_date=datetime(2025, 11, 7, 19, 0),
                completed=True
            ),
            Workout(
                name="Core Focus",
                exercises_used="Planks, Leg Raises, Russian Twists",
                scheduled_date=datetime(2025, 11, 5, 18, 45),
                completed=True
            )
        ]
        db.session.add_all(workouts)
        db.session.commit()
        print(f"  Seeded {len(workouts)} workouts")

        print("Seeding Goals...")
        goals = [
            Goal(
                title="100 Push-ups in a Row",
                description="Complete 100 consecutive push-ups",
                status="completed",
                progress_percent=100,
                progress_text="100/100 push-ups",
                target_date=date(2025, 12, 15),
                media_count_photos=5,
                media_count_videos=2
            ),
            Goal(
                title="First Muscle-up",
                description="Perform a clean muscle-up on rings",
                status="in_progress",
                progress_percent=65,
                progress_text="65% Progress",
                target_date=date(2026, 1, 10),
                media_count_photos=3,
                media_count_videos=1
            ),
            Goal(
                title="Handstand Hold - 60 Seconds",
                description="Hold a freestanding handstand for 60 seconds",
                status="in_progress",
                progress_percent=42,
                progress_text="25/60 seconds",
                target_date=date(2026, 2, 1),
                media_count_photos=2,
                media_count_videos=0
            ),
            Goal(
                title="Planche Progression",
                description="Achieve a full planche hold",
                status="not_started",
                progress_percent=0,
                progress_text="0% Progress",
                target_date=date(2026, 2, 1),
                media_count_photos=0,
                media_count_videos=0
            )
        ]
        db.session.add_all(goals)
        db.session.commit()
        print(f"  Seeded {len(goals)} goals")

        print("Seeding Plans...")
        plans = [
            Plan(
                title="Upper Body Strength",
                plan_type="strength",
                start_date=date(2025, 11, 1),
                end_date=date(2025, 11, 30),
                description="Build upper body strength with progressive overload",
                status="completed",
                progress_percent=100
            ),
            Plan(
                title="Core Development",
                plan_type="strength",
                start_date=date(2025, 11, 5),
                end_date=date(2025, 11, 25),
                description="Develop core stability and strength",
                status="completed",
                progress_percent=100
            ),
            Plan(
                title="Skill Progression",
                plan_type="skill",
                start_date=date(2025, 11, 10),
                end_date=date(2025, 12, 10),
                description="Master advanced calisthenics skills",
                status="in_progress",
                progress_percent=60
            ),
            Plan(
                title="Flexibility & Mobility",
                plan_type="flexibility",
                start_date=date(2025, 11, 15),
                end_date=date(2025, 12, 15),
                description="Improve flexibility and joint mobility",
                status="upcoming",
                progress_percent=0
            ),
            Plan(
                title="Endurance Training",
                plan_type="endurance",
                start_date=date(2025, 11, 20),
                end_date=date(2025, 12, 20),
                description="Build muscular endurance with high reps",
                status="upcoming",
                progress_percent=0
            )
        ]
        db.session.add_all(plans)
        db.session.commit()
        print(f"  Seeded {len(plans)} plans")

        print("Seeding Schedule Items...")
        schedule_items = [
            ScheduleItem(day_of_week="Monday", time="6:30PM", name="Upper Body", details="workout", item_type="workout"),
            ScheduleItem(day_of_week="Monday", time="8:00PM", name="Mobility", details="workout", item_type="workout"),
            ScheduleItem(day_of_week="Tuesday", time="7:00PM", name="Leg Day", details="workout", item_type="workout"),
            ScheduleItem(day_of_week="Wednesday", time="6:45PM", name="Core Focus", details="workout", item_type="workout"),
            ScheduleItem(day_of_week="Wednesday", time="8:30PM", name="Skill Work", details="workout", item_type="workout"),
            ScheduleItem(day_of_week="Thursday", time="All Day", name="Active Rest", details="rest", item_type="rest"),
            ScheduleItem(day_of_week="Friday", time="7:15PM", name="Full Body", details="workout", item_type="workout"),
            ScheduleItem(day_of_week="Saturday", time="9:00AM", name="Outdoor Workout", details="workout", item_type="workout"),
            ScheduleItem(day_of_week="Saturday", time="3:00PM", name="Recovery", details="rest", item_type="rest"),
            ScheduleItem(day_of_week="Sunday", time="All Day", name="Complete Rest", details="rest", item_type="rest")
        ]
        db.session.add_all(schedule_items)
        db.session.commit()
        print(f"  Seeded {len(schedule_items)} schedule items")

        print("Seeding Calendar Events...")
        calendar_events = [
            CalendarEvent(date=date(2025, 11, 1), event_type="workout", name="Upper Body"),
            CalendarEvent(date=date(2025, 11, 3), event_type="workout", name="Leg Day"),
            CalendarEvent(date=date(2025, 11, 5), event_type="workout", name="Core Focus"),
            CalendarEvent(date=date(2025, 11, 7), event_type="workout", name="Full Body"),
            CalendarEvent(date=date(2025, 11, 8), event_type="workout", name="Upper Body"),
            CalendarEvent(date=date(2025, 11, 10), event_type="rest", name="Rest Day"),
            CalendarEvent(date=date(2025, 11, 12), event_type="workout", name="Push Day"),
            CalendarEvent(date=date(2025, 11, 14), event_type="workout", name="Pull Day"),
            CalendarEvent(date=date(2025, 11, 15), event_type="tournament", name="Tournament"),
            CalendarEvent(date=date(2025, 11, 18), event_type="workout", name="Leg Day"),
            CalendarEvent(date=date(2025, 11, 20), event_type="rest", name="Rest Day"),
            CalendarEvent(date=date(2025, 11, 22), event_type="planned", name="Skill Day")
        ]
        db.session.add_all(calendar_events)
        db.session.commit()
        print(f"  Seeded {len(calendar_events)} calendar events")

        print("Seeding Health Records...")
        health_records = [
            HealthRecord(date=date(2025, 11, 1), weight=75.0, height=175.0, age=25, gender="Male", body_fat=18.5),
            HealthRecord(date=date(2025, 11, 5), weight=74.8, height=175.0, age=25, gender="Male", body_fat=18.2),
            HealthRecord(date=date(2025, 11, 10), weight=74.5, height=175.0, age=25, gender="Male", body_fat=17.9),
            HealthRecord(date=date(2025, 11, 15), weight=74.2, height=175.0, age=25, gender="Male", body_fat=17.6),
            HealthRecord(date=date(2025, 11, 20), weight=74.0, height=175.0, age=25, gender="Male", body_fat=17.3)
        ]
        for record in health_records:
            record.calculate_bmi()
        db.session.add_all(health_records)
        db.session.commit()
        print(f"  Seeded {len(health_records)} health records")

        print("Seeding Health Plan Items...")
        health_plan_items = [
            HealthPlanItem(title="Increase Protein Intake", description="Add 20g more protein daily", completed=True),
            HealthPlanItem(title="Sleep Optimization", description="Get 8 hours of sleep every night", completed=False),
            HealthPlanItem(title="Hydration Goal", description="Drink 3 liters of water daily", completed=True),
            HealthPlanItem(title="Stretching Routine", description="15 minutes of stretching every morning", completed=False)
        ]
        db.session.add_all(health_plan_items)
        db.session.commit()
        print(f"  Seeded {len(health_plan_items)} health plan items")

        print("Seeding User Level...")
        user_level = UserLevel(
            current_level=27,
            rank_name="Bronze Elite",
            current_xp=7342,
            max_xp=10000,
            tournaments_participated=12,
            wins=8,
            global_rank=24,
            win_streak=3,
            level_history=json.dumps([
                {"month": "Jun", "level": 20},
                {"month": "Jul", "level": 21},
                {"month": "Aug", "level": 23},
                {"month": "Sep", "level": 24},
                {"month": "Oct", "level": 26},
                {"month": "Nov", "level": 27}
            ])
        )
        db.session.add(user_level)
        db.session.commit()
        print("  Seeded 1 user level")

        print("Seeding Tournament Challenges...")
        tournament_challenges = [
            TournamentChallenge(
                title="Push-up Endurance",
                level_required=25,
                status="active",
                details=json.dumps({"pushups": "100", "sets": "1", "rest": "None"}),
                time_limit="5 minutes"
            ),
            TournamentChallenge(
                title="Pull-up Test",
                level_required=20,
                status="active",
                details=json.dumps({"pullups": "20", "sets": "1", "rest": "None"}),
                time_limit="3 minutes"
            ),
            TournamentChallenge(
                title="Core Gauntlet",
                level_required=22,
                status="active",
                details=json.dumps({"plank": "3min", "leg_raises": "20", "russian_twists": "30"}),
                time_limit="10 minutes"
            ),
            TournamentChallenge(
                title="Muscle-up Challenge",
                level_required=27,
                status="locked",
                details=json.dumps({"muscleups": "5", "sets": "1", "rest": "None"}),
                time_limit="5 minutes"
            )
        ]
        db.session.add_all(tournament_challenges)
        db.session.commit()
        print(f"  Seeded {len(tournament_challenges)} tournament challenges")

        print("Seeding Videos...")
        videos = [
            Video(
                title="Beginner Push-up Tutorial",
                description="Learn proper push-up form",
                category="tutorial",
                duration="12:34",
                views="15.2K",
                likes=342,
                upload_date=date(2025, 11, 1),
                thumbnail_gradient="linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
            ),
            Video(
                title="Pull-up Progression Guide",
                description="From zero to 20 pull-ups",
                category="tutorial",
                duration="18:45",
                views="23.1K",
                likes=567,
                upload_date=date(2025, 11, 5),
                thumbnail_gradient="linear-gradient(135deg, #f093fb 0%, #f5576c 100%)"
            ),
            Video(
                title="Full Body HIIT Workout",
                description="30-minute intense workout",
                category="workout",
                duration="32:10",
                views="45.6K",
                likes=891,
                upload_date=date(2025, 11, 8),
                thumbnail_gradient="linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)"
            ),
            Video(
                title="My 6 Month Transformation",
                description="Calisthenics progress update",
                category="progress",
                duration="8:22",
                views="8.9K",
                likes=234,
                upload_date=date(2025, 11, 12),
                thumbnail_gradient="linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)"
            ),
            Video(
                title="Handstand Basics",
                description="Master the handstand kick-up",
                category="tutorial",
                duration="15:30",
                views="18.7K",
                likes=445,
                upload_date=date(2025, 11, 15),
                thumbnail_gradient="linear-gradient(135deg, #fa709a 0%, #fee140 100%)"
            ),
            Video(
                title="Morning Motivation",
                description="Start your day right",
                category="motivation",
                duration="5:15",
                views="12.3K",
                likes=678,
                upload_date=date(2025, 11, 18),
                thumbnail_gradient="linear-gradient(135deg, #a18cd1 0%, #fbc2eb 100%)"
            )
        ]
        db.session.add_all(videos)
        db.session.commit()
        print(f"  Seeded {len(videos)} videos")

        print("Seeding Motivation Items...")
        motivations = [
            Motivation(
                title="Calisthenics Mastery",
                description="Complete guide to bodyweight training",
                category="video",
                author="Fitness Pro",
                duration_or_pages="45 min",
                gradient="linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
                is_favorite=True
            ),
            Motivation(
                title="The Bodyweight Solution",
                description="Transform your body without equipment",
                category="book",
                author="Mark Lauren",
                duration_or_pages="320 pages",
                gradient="linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
                is_favorite=False
            ),
            Motivation(
                title="Discipline Equals Freedom",
                description="Build mental toughness through training",
                category="quote",
                author="Jocko Willink",
                duration_or_pages="",
                gradient="linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
                is_favorite=True
            ),
            Motivation(
                title="Warrior Workout",
                description="Advanced bodyweight training program",
                category="video",
                author="Alex Silver-Fagan",
                duration_or_pages="60 min",
                gradient="linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)",
                is_favorite=False
            ),
            Motivation(
                title="Overcoming Gravity",
                description="Complete guide to bodyweight strength",
                category="book",
                author="Steven Low",
                duration_or_pages="456 pages",
                gradient="linear-gradient(135deg, #fa709a 0%, #fee140 100%)",
                is_favorite=False
            ),
            Motivation(
                title="Consistency is Key",
                description="The power of daily habits",
                category="quote",
                author="Unknown",
                duration_or_pages="",
                gradient="linear-gradient(135deg, #a18cd1 0%, #fbc2eb 100%)",
                is_favorite=True
            ),
            Motivation(
                title="The Journey Begins",
                description="Documentary about calisthenics athletes",
                category="movie",
                author="Street Workout Films",
                duration_or_pages="90 min",
                gradient="linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)",
                is_favorite=False
            ),
            Motivation(
                title="Mind Muscle Connection",
                description="Podcast about training psychology",
                category="podcast",
                author="Mind Pump",
                duration_or_pages="55 min",
                gradient="linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)",
                is_favorite=False
            )
        ]
        db.session.add_all(motivations)
        db.session.commit()
        print(f"  Seeded {len(motivations)} motivation items")

        print("Seeding Sticky Notes...")
        sticky_notes = [
            StickyNote(title="Form Check", content="Review push-up form video", color="yellow"),
            StickyNote(title="Progress Goal", content="Update muscle-up progress tracker", color="orange"),
            StickyNote(title="Rest Priority", content="Schedule rest day this week", color="pink"),
            StickyNote(title="Meal Prep", content="Prepare high-protein meals", color="green")
        ]
        db.session.add_all(sticky_notes)
        db.session.commit()
        print(f"  Seeded {len(sticky_notes)} sticky notes")

        print("\nDatabase seeding complete!")


if __name__ == '__main__':
    seed_database()
