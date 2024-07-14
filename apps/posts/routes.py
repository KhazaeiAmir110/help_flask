from flask import Blueprint

blueprint = Blueprint('posts', __name__)


@blueprint.route('/posts', methods=['GET'])
def get_posts():
    return 'POSTS'
