from flask import Blueprint

blueprint = Blueprint('users', __name__)


@blueprint.route('/login', methods=['post', 'GET'])
def login_user():
    return '<h1>Hello Users!</h1>'
