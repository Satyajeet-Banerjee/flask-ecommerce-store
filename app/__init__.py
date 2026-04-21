from flask import Flask
from .extensions import db, login_manager
from .models.user import User
from app.models.cart_item import CartItem
from flask_login import current_user
def create_app():
    app = Flask(__name__)

    app.config.from_object("config.Config")

    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes.auth import auth_bp
    from .routes.store import store_bp
    from .routes.cart import cart_bp
    from .routes.payment import payment_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(store_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(payment_bp)

    @app.context_processor
    def inject_cart_count():
        if current_user.is_authenticated:
            count = sum(item.quantity for item in CartItem.query.filter_by(user_id=current_user.id).all())
        else:
            count = 0

        return dict(cart_count=count)

    return app