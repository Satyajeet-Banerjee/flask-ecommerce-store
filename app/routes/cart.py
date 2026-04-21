from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_required, current_user
from app.extensions import db
from app.models.cart_item import CartItem

cart_bp = Blueprint("cart", __name__, url_prefix="/cart")


@cart_bp.route("/add/<int:product_id>")
@login_required
def add_to_cart(product_id):
    item = CartItem.query.filter_by(
        user_id=current_user.id,
        product_id=product_id
    ).first()

    if item:
        item.quantity += 1
    else:
        item = CartItem(user_id=current_user.id, product_id=product_id)
        db.session.add(item)

    db.session.commit()
    return redirect(url_for("store.home"))


@cart_bp.route("/")
@login_required
def view_cart():
    items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = sum(item.product.price * item.quantity for item in items)

    return render_template("cart.html", items=items, total=total)

@cart_bp.route("/increase/<int:item_id>")
@login_required
def increase_quantity(item_id):
    item = CartItem.query.get_or_404(item_id)

    if item.user_id == current_user.id:
        item.quantity += 1
        db.session.commit()

    return redirect(url_for("cart.view_cart"))


@cart_bp.route("/decrease/<int:item_id>")
@login_required
def decrease_quantity(item_id):
    item = CartItem.query.get_or_404(item_id)

    if item.user_id == current_user.id:
        if item.quantity > 1:
            item.quantity -= 1
        else:
            db.session.delete(item)

        db.session.commit()

    return redirect(url_for("cart.view_cart"))


@cart_bp.route("/remove/<int:item_id>")
@login_required
def remove_item(item_id):
    item = CartItem.query.get_or_404(item_id)

    if item.user_id == current_user.id:
        db.session.delete(item)
        db.session.commit()

    return redirect(url_for("cart.view_cart"))