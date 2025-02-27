from flask import Blueprint, render_template, redirect

from ..forms import RegistrationForm
from ..models.user import User
from ..extensions import db, bcrypt

user = Blueprint('user', __name__)


@user.route('/user/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # Если форма валидна
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, login=form.login.data, avatar=form.avatar.data, password=hashed_password)
    return render_template('user/register.html', form=form)
