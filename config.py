import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "devkey")

    SQLALCHEMY_DATABASE_URI = "sqlite:///ecommerce.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
    RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET")