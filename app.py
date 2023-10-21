from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<string:name>')  # address type one
def home(name):
    context = {
        'name': name,
        'title': 'home',
        'active_home': 'active',
    }
    return render_template('home.html', **context)


def about():
    context = {
        'title': 'about',
        'name': 'about',
        'active_about': 'active',
    }
    return render_template('home.html', **context)


app.add_url_rule(rule='/about/', view_func=about)  # address type two

if __name__ == '__main__':
    app.run(debug=True)
