from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', name='amir', title='home')


@app.route('/about')
def about():
    return render_template('about.html', title='about')
