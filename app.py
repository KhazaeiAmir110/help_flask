from flask import Flask, render_template, request

import conf.config as conf
import conf.functions as fun

app = Flask(__name__)


@app.route('/')
def Home():
    if request.args.get('search'):
        pass
    elif request.args.get('category_id'):
        pass
    else:
        articles = fun.get_articles()

    return render_template(
        'home.html',
        site_title = conf.SITE_TITLE,
        categories = fun.get_categories(),
        articles = articles
    )

if __name__ == '__main__':
    app.run(debug=True)
