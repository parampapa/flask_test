import os

from flask import Flask
from .extensions import db, migrate, bcrypt
from .routes.user import user
from .routes.post import post


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback-secret-key')

    app.register_blueprint(user)
    app.register_blueprint(post)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    return app
