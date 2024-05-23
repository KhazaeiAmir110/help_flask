from flask import (
    Flask, render_template, request, abort, session, url_for, flash, redirect)
from flask_login import (
    LoginManager, login_user, logout_user, login_required, current_user, UserMixin)

from conf import config as conf
from conf import functions as fun

app = Flask(__name__)


@app.route('/')
def Home():
    if request.args.get('search'):
        articles = fun.get_article_with_search(searched_word=request.args.get('search'))
    elif request.args.get('category_id'):
        articles = fun.get_article_with_category_id(category_id=request.args.get('category_id'))
    else:
        articles = fun.get_articles()

    return render_template(
        'home.html',
        site_title=conf.SITE_TITLE,
        categories=fun.get_categories(),
        articles=articles
    )


@app.route('/single/<int:id>')
def Article(id):
    if not fun.get_article_by_id(id):
        abort(404, 'Article not found')
    article = fun.get_article_by_id(id)
    return render_template(
        'single.html',
        article=article,
        article_category=fun.get_categories_by_id(article[4])
    )


# Login

# setting login
app.config.update(SECRET_KEY=conf.SECRET_KEY)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User
class User(UserMixin):
    def __init__(self):
        self.id = id

    def __repr__(self):
        return self.id


user = User(0)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return url_for('dashboard')
    elif request.method == 'POST':
        if (not request.form['username']) or (not request.form['password']):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        elif (request.form['username']!= conf.ADMIN_USERNAME or request.form['password']!= conf.ADMIN_PASSWORD):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        flash('You are now logged in')
        return redirect(url_for('dashboard'))

    elif session.get():
        pass


@app.route('/dashboard')
def dashboard():
    return 'Hello World!'

@login_manager.user_loader
def load_user(id):
    return User(id)


if __name__ == '__main__':
    app.run()
