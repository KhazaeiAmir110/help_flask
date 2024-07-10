from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.app_context().push()


# models
class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    context = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'Text(id={self.id}, context={self.context})'


@app.route('/')
def home():
    messages = Text.query.filter(Text.id == 1).first()
    context = {
        'message': messages,
        'name': 'amir'
    }
    return render_template('home.html', context=context, title='Home')


@app.route('/about')
def about():
    messages = Text.query.filter(Text.id == 2).first()
    context = {
        'title': 'About',
        'message': messages
    }
    return render_template('about.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)
