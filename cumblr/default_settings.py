import os

UPLOAD_FOLDER = 'cumblr/uploads'

DEBUG = os.environ.get('DEBUG', False)

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://Odysseus@localhost/maple')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('DEBUG', False)
