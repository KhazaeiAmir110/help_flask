from flask import Flask, render_template

import conf.config as conf
import conf.functions as fun

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    vis = {
        'site_title' : conf.SITE_TITLE,
        'categories' : fun.get_categories()

    }
    return render_template(
        'home.html',
        site_title = conf.SITE_TITLE,
        categories = fun.get_categories()
    )

if __name__ == '__main__':
    app.run(debug=True)
