import os

basedir = os.path.abspath(os.path.dirname(__file__))

# On Vercel, use /tmp for writable storage
is_vercel = os.environ.get('VERCEL', False)
db_dir = '/tmp' if is_vercel else os.path.join(basedir, 'instance')


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(db_dir, 'calisthenics.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(basedir, 'static', 'images', 'uploads') if not is_vercel else '/tmp/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
