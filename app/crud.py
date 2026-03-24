from app.models import Product, Base
from app.db import engine, SessionLocal

# إنشاء الجداول
Base.metadata.create_all(engine)

def add_product(name, price):
    session = SessionLocal()
    product = Product(name=name, price=price)
    session.add(product)
    session.commit()
    product_data = {"id": product.id, "name": product.name, "price": product.price}
    session.close()
    return product_data

def list_products():
    session = SessionLocal()
    products = session.query(Product).all()
    data = [{"id": p.id, "name": p.name, "price": p.price} for p in products]
    session.close()
    return data

def get_product(product_id):
    session = SessionLocal()
    product = session.query(Product).get(product_id)
    data = {"id": product.id, "name": product.name, "price": product.price} if product else None
    session.close()
    return data

def update_product(product_id, new_name, new_price):
    session = SessionLocal()
    product = session.query(Product).get(product_id)
    if product:
        product.name = new_name
        product.price = new_price
        session.commit()
        data = {"id": product.id, "name": product.name, "price": product.price}
    else:
        data = None
    session.close()
    return data

def delete_product(product_id):
    session = SessionLocal()
    product = session.query(Product).get(product_id)
    if product:
        session.delete(product)
        session.commit()
        result = True
    else:
        result = False
    session.close()
    return result

def reset_products():
    session = SessionLocal()
    session.query(Product).delete()
    session.commit()
    session.close()