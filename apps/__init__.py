from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from apps.users.routes import blueprint as users_blueprint
from apps.posts.routes import blueprint as posts_blueprint
from base import exceptions as app_exception

app = Flask(__name__)


# routes
def register_blueprints(app):
    app.register_blueprint(users_blueprint)
    app.register_blueprint(posts_blueprint)


register_blueprints(app)

# config
app.config.from_object('base.config.DevelopmentConfig')

# db
app.app_context().push()
db = SQLAlchemy(app)

from apps.users.models import User

migrate = Migrate(app, db)


# exception
def register_error_handlers(app):
    app.register_error_handler(404, app_exception.page_not_found)
    app.register_error_handler(500, app_exception.server_error)


register_error_handlers(app)
