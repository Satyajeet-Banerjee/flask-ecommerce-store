from app.extensions import db
from datetime import datetime,UTC

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    total_amount = db.Column(db.Integer)

    status = db.Column(db.String(50), default="Pending")

    created_at = db.Column(db.DateTime, default=datetime.now(UTC))

    items = db.relationship('OrderItem', backref='order', lazy=True)