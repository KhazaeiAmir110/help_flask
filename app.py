from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    context = {
        'message': 'Hello World!',
        'name': 'amir'
    }
    return render_template('home.html', context=context, title='Home')


@app.route('/about')
def about():
    context = {
        'title': 'About',
        'message': 'This is an About!'
    }
    return render_template('about.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)
