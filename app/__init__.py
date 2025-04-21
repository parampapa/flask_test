import os

from flask import Flask
from .extensions import db, migrate, bcrypt, login_manager
from .routes.user import user
from .routes.post import post
from .config import Config


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback-secret-key')

    app.register_blueprint(user)
    app.register_blueprint(post)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    #LOGIN MANAGER
    login_manager.login_view = 'user.login'
    login_manager.login_message_category = 'У вас нет доступа сначала авторизуйтесь на сайте'
    login_manager.login_message_category = 'info'

    with app.app_context():
        db.create_all()

    return app
