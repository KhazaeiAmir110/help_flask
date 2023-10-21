from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
