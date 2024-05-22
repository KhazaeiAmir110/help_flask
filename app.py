from flask import Flask, render_template, request, abort

import conf.config as conf
import conf.functions as fun

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
        site_title = conf.SITE_TITLE,
        categories = fun.get_categories(),
        articles = articles
    )

@app.route('/single/<int:id>')
def Article(id):
    if not fun.get_article_by_id(id):
        abort(404, 'Article not found')
    return render_template(
        'single.html',
        article = fun.get_article_by_id(id)
    )

if __name__ == '__main__':
    app.run()
