from flask import Flask

from apps.users.routes import blueprint as users_blueprint
from apps.posts.routes import blueprint as posts_blueprint


app = Flask(__name__)

# routes
app.register_blueprint(users_blueprint)
app.register_blueprint(posts_blueprint)


# config
app.config.from_object('base.config.DevelopmentConfig')
