from flask import Blueprint
from ..models.user import User
from ..extensions import db

user = Blueprint('user', __name__)


@user.route('/user/register', methods=['GET', 'POST'])
def create_user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return f"User '{name}' created successfully."
