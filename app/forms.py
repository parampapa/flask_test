from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    name = StringField('ФИО', [InputRequired(), Length(min=1, max=50)])
    login = StringField('Логин', [InputRequired(), Length(min=1, max=50)])
    password = PasswordField('Пароль', [InputRequired(), Length(min=8, max=200)])
    confirm_password = PasswordField('Подтверждение пароля', [InputRequired(), Length(min=8, max=200), EqualTo('password')])
    submit = StringField('Зарегистрироваться')