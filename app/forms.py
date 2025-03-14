from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.fields.simple import StringField, PasswordField, FileField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired
from wtforms.widgets.core import SubmitInput


class RegistrationForm(FlaskForm):
    name = StringField('ФИО', [DataRequired(), Length(min=1, max=50)])
    login = StringField('Логин', [DataRequired(), Length(min=1, max=20)])
    password = PasswordField('Пароль', [DataRequired(), Length(min=1, max=200)])
    confirm_password = PasswordField('Подтверждение пароля', [DataRequired(), Length(min=1, max=200), EqualTo('password')])
    avatar = FileField('Загрузите фото', [
        FileRequired(message="Файл обязателен!"),
        FileAllowed(['jpg', 'jpeg', 'png'],
                    message="Только изображения JPG, JPEG, PNG!")
    ])
    submit = SubmitField('Зарегистрироваться')
