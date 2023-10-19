from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///simple.db"
db = SQLAlchemy(app)


class SimpleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    data = db.Column(db.DateTime(timezone=True))

    def __repr__(self):
        return f'simple :\n id: {self.id} \n name : {self.name} \n text : {self.description} \n ' \
               f'time : {self.data} '


@app.route('/')
@app.route('/home')
def hello_world():
    context = {
        'name': 'amir',
        'title': 'home',
        'active_home': 'active',
    }
    return render_template('home.html', **context)


@app.route('/about')
def about():
    context = {
        'title': 'about',
        'active_about': 'active',
    }
    return render_template('about.html', **context)


if __name__ == '__main__':
    app.run(debug=True, )
