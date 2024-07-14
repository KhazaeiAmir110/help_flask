from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from apps.users.routes import blueprint as users_blueprint
from apps.posts.routes import blueprint as posts_blueprint

app = Flask(__name__)


# routes
def register_blueprints(app):
    app.register_blueprint(users_blueprint)
    app.register_blueprint(posts_blueprint)


register_blueprints(app)

# config
app.config.from_object('base.config.DevelopmentConfig')

# db
db = SQLAlchemy(app)
db.create_all()
