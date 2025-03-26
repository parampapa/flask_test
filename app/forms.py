from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.fields.simple import StringField, PasswordField, FileField, \
    SubmitField, BooleanField
from wtforms.validators import Length, EqualTo, DataRequired, ValidationError

from .models.user import User


class RegistrationForm(FlaskForm):
    name = StringField('ФИО', [DataRequired(), Length(min=1, max=50)])
    login = StringField('Логин', [DataRequired(), Length(min=1, max=20)])
    password = PasswordField('Пароль',
                             [DataRequired(), Length(min=3, max=200)])
    confirm_password = PasswordField('Подтверждение пароля',
                                     [DataRequired(), Length(min=3, max=200),
                                      EqualTo('password')])
    avatar = FileField('Загрузите фото', [
        FileRequired(message="Файл обязателен!"),
        FileAllowed(['jpg', 'jpeg', 'png'],
                    message="Только изображения JPG, JPEG, PNG!")
    ])
    submit = SubmitField('Зарегистрироваться')

    def validate_login(self, login):
        if User.query.filter_by(login=login.data).first():
            raise ValidationError('Логин уже занят.')


class LoginForm(FlaskForm):
    login = StringField('Логин', [DataRequired(), Length(min=1, max=20)])
    password = PasswordField('Пароль',
                             [DataRequired(), Length(min=3, max=200)])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
