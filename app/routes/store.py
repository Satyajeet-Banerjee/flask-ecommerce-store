from flask import Blueprint, render_template
from app.models.product import Product
from flask_login import login_required, current_user
from app.models.order import Order

store_bp = Blueprint("store", __name__)


@store_bp.route("/")
def home():
    products = Product.query.all()
    return render_template("home.html", products=products)


@store_bp.route("/product/<int:id>")
def product_detail(id):
    product = Product.query.get_or_404(id)
    return render_template("product.html", product=product)

@store_bp.route("/orders")
@login_required
def orders():
    user_orders = Order.query.filter_by(user_id=current_user.id)\
                             .order_by(Order.created_at.desc())\
                             .all()

    return render_template("orders.html", orders=user_orders)