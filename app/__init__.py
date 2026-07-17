from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    import os
    basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    app = Flask(__name__, template_folder=os.path.join(basedir, 'templates'),
                static_folder=os.path.join(basedir, 'static'))
    app.config.from_object('config.Config')

    db.init_app(app)

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

    with app.app_context():
        from app.models import user, workout, goal, plan, schedule, health, tournament, video, motivation, calendar_event  # noqa: F401
        db.create_all()

    @app.errorhandler(404)
    def not_found(e):
        from flask import render_template
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def server_error(e):
        from flask import render_template
        return render_template('500.html'), 500

    return app
