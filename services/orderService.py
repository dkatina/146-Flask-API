from models.order import Order
from datetime import date
from sqlalchemy import select
from database import db
from models.product import Product
from models.customer import Customer


def save(order_data):
    new_order = Order(date=date.today(), customer_id = order_data['customer_id'])

    for item_id in order_data['product_ids']:
        query = select(Product).filter(Product.id == item_id)
        item = db.session.execute(query).scalar()
        print(item)
        new_order.products.append(item)
    
    db.session.add(new_order)
    db.session.commit()

    db.session.refresh(new_order)
    return new_order

def find_all():
    query = select(Order)
    all_orders = db.session.execute(query).scalars().all()
    return all_orders

def find_by_id(id):
    query = select(Order).filter(Order.id==id)
    orders = db.session.execute(query).scalars().all()
    return orders

def find_by_customer_id(id):
    query = select(Order).filter(Order.customer_id==id)
    orders = db.session.execute(query).scalars().all()
    return orders

def find_by_customer_email(email):
    query = select(Order).join(Customer).where(Customer.id==Order.customer_id).filter(Customer.email == email)
    orders = db.session.execute(query).scalars().all()
    return orders