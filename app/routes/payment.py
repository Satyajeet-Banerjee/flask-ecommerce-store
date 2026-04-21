import razorpay
from flask import Blueprint, render_template, current_app, request, redirect, url_for
from flask_login import login_required, current_user
from app.models.cart_item import CartItem
from app.extensions import db
from app.models.order import Order
from app.models.order_item import OrderItem


# ✅ CHECKOUT
payment_bp = Blueprint("payment", __name__, url_prefix="/payment")

@payment_bp.route("/checkout")
@login_required
def checkout():
    items = CartItem.query.filter_by(user_id=current_user.id).all()

    if not items:
        return redirect(url_for("cart.view_cart"))

    total = sum(item.product.price * item.quantity for item in items)

    client = razorpay.Client(auth=(
        current_app.config["RAZORPAY_KEY_ID"],
        current_app.config["RAZORPAY_KEY_SECRET"]
    ))

    order = client.order.create({
        "amount": total,  # in paise
        "currency": "INR",
        "payment_capture": 1
    })

    return render_template(
        "payment.html",
        order_id=order["id"],
        amount=total,
        key_id=current_app.config["RAZORPAY_KEY_ID"],
        user=current_user
    )


# ✅ SUCCESS
@payment_bp.route("/success")
@login_required
def success():
    items = CartItem.query.filter_by(user_id=current_user.id).all()

    if not items:
        return redirect(url_for("store.home"))

    total = sum(item.product.price * item.quantity for item in items)

    order = Order(user_id=current_user.id, total_amount=total)
    db.session.add(order)
    db.session.flush()

    for item in items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.product.price
        )
        db.session.add(order_item)

    for item in items:
        db.session.delete(item)

    db.session.commit()

    return redirect(url_for("store.orders"))


# ✅ CANCEL
@payment_bp.route("/cancel")
@login_required
def cancel():
    return redirect(url_for("cart.view_cart"))