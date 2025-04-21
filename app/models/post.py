from datetime import datetime, UTC

from ..extensions import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher = db.Column(db.Integer,
                        db.ForeignKey('user.id', ondelete='CASCADE'))
    student = db.Column(db.Integer)
    subject = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime,
                     default=lambda: datetime.now(UTC))  # Новый вариант с UTC
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC),
                           onupdate=lambda: datetime.now(
                               UTC))  # Дата обновления
