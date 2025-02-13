from datetime import datetime

from ..extensions import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher = db.Column(db.String(255), nullable=False)
    student = db.Column(db.String(255), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow)
