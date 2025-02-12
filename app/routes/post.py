from flask import Blueprint
from ..models.post import Post
from ..extensions import db

post = Blueprint('post', __name__)


@post.route('/post/<subject>')
def create_post(subject):
    post = Post(subject=subject)
    db.session.add(post)
    db.session.commit()
    return f"Post '{subject}' created successfully."
