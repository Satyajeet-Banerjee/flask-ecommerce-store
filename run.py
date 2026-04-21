from app import create_app
from app.extensions import db
from app.models.product import Product

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        #Dummy products
        if Product.query.count() == 0:
            products = [
                Product(
                    name="iPhone 14",
                    price=7990000,
                    description="Apple smartphone with A15 chip",
                    image_url="https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"
                ),
                Product(
                    name="Gaming Laptop",
                    price=12000000,
                    description="High performance laptop for gaming",
                    image_url="https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400"
                ),
                Product(
                    name="Wireless Headphones",
                    price=199900,
                    description="Noise cancelling headphones",
                    image_url="https://images.unsplash.com/photo-1518444065439-e933c06ce9cd?w=400"
                ),
                Product(
                    name="Smart Watch",
                    price=499900,
                    description="Track fitness and health",
                    image_url="https://images.unsplash.com/photo-1517433456452-f9633a875f6f?w=400"
                ),
                Product(
                    name="DSLR Camera",
                    price=6500000,
                    description="Professional photography camera",
                    image_url="https://images.unsplash.com/photo-1495707902641-75cac588d2e9?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                ),
                Product(
                    name="Bluetooth Speaker",
                    price=299900,
                    description="Portable speaker with deep bass",
                    image_url="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400"
                ),
                Product(
                    name="Mechanical Keyboard",
                    price=89900,
                    description="RGB gaming keyboard",
                    image_url="https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400"
                ),
                Product(
                    name="Gaming Mouse",
                    price=49900,
                    description="High precision gaming mouse",
                    image_url="https://images.unsplash.com/photo-1587202372775-e229f172b9d7?w=400"
                ),
                Product(
                    name="LED Monitor",
                    price=1500000,
                    description="24-inch full HD monitor",
                    image_url="https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=400"
                ),
                Product(
                    name="Tablet",
                    price=3500000,
                    description="Portable tablet for work and play",
                    image_url="https://images.unsplash.com/photo-1580910051074-3eb694886505?w=400"
                )
            ]

            db.session.bulk_save_objects(products)
            db.session.commit()

    app.run(debug=True)