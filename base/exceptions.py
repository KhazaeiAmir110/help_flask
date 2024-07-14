from flask import render_template


def page_not_found(e):
    return render_template('base/404.html'), 404


def server_error(e):
    return render_template('base/500.html'), 500