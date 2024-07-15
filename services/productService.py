from models.product import Product
from database import db
from sqlalchemy import select


def save(product_data):
    new_product = Product(name=product_data['name'], price=product_data['price'])
    db.session.add(new_product)
    db.session.commit()
    db.session.refresh(new_product)    
    return new_product

def find_all():
    query = select(Product)
    all_productss = db.session.execute(query).scalars().all()
    return all_productss