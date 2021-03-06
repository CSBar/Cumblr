from flask import Flask
from cumblr.database import db
from cumblr.keys import APP_SECRET_KEY
from werkzeug.contrib.fixers import ProxyFix
from raven.contrib.flask import Sentry

## initialize app
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
Sentry(app)
app.secret_key = keys.APP_SECRET_KEY
app.config.from_pyfile('default_settings.py')

from cumblr import views
from cumblr import filters
from cumblr import admin
from .manager import twitter_blueprint, google_blueprint, login_manager

# hook up extensions
app.register_blueprint(twitter_blueprint, url_prefix='/login')
app.register_blueprint(google_blueprint, url_prefix='/login')
db.init_app(app)
login_manager.init_app(app)
