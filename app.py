from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite3'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.column(db.String(50))
    email = db.column(db.String(100))
    password = db.Column(db.String(50))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f'{self.username}'


@app.route('/<string:name>')  # address type one
def home(name):
    context = {
        'name': name,
        'title': 'home',
        'active_home': 'active',
    }
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return render_template('home.html', **context)


def about():
    context = {
        'title': 'about',
        'name': 'about',
        'active_about': 'active',
    }
    return render_template('home.html', **context)


app.add_url_rule(rule='/about/', view_func=about)  # address type two


@app.route('/admin')
def admin():
    return 'HELLO ADMIN'


@app.route('/login', methods=['POST', 'GET'])
def login():
    context = {
        'title': 'login',
        'name': 'login',
        'active_about': 'active',
    }
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        return f"<h3>login page :</h3> \n username : {username} email : {email}"
    else:
        return render_template('login.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
