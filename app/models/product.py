from app.extensions import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Integer, nullable=False)  # in paise
    description = db.Column(db.Text)
    image_url = db.Column(
        db.String(300),
        default="https://via.placeholder.com/300"
    )