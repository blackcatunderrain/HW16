import json
import os
from config import db
from models import Order, Offer, User


def insert_data_user(input_data):
    for raw in input_data:
        db.session.add(
            User(
                id=raw.get('id'),
                first_name=raw.get('first_name'),
                last_name=raw.get('last_name'),
                age=raw.get('age'),
                email=raw.get('email'),
                role=raw.get('role'),
                phone=raw.get('phone')
            )
        )
    db.session.commit()


def insert_data_order(input_data):
    for raw in input_data:
        db.session.add(
            Order(
                id=raw.get('id'),
                name=raw.get('name'),
                description=raw.get('description'),
                start_date=raw.get('start_date'),
                end_date=raw.get('end_date'),
                address=raw.get('address'),
                price=raw.get('price'),
                customer_id=raw.get('customer_id'),
                executor_id=raw.get('executor_id')
            )
        )
    db.session.commit()


def insert_data_offer(input_data):
    for raw in input_data:
        db.session.add(
            Offer(
                id=raw.get('id'),
                order_id=raw.get('order_id'),
                executor_id=raw.get('executor_id'),
            )
        )
    db.session.commit()


def init_db():
    db.drop_all()
    db.create_all()
    with open(os.path.join("data", "users.json"), encoding="UTF-8") as f:
        insert_data_user(json.load(f))

    with open(os.path.join("data", "orders.json"), encoding="UTF-8") as f:
        insert_data_order(json.load(f))

    with open(os.path.join("data", "offers.json"), encoding="UTF-8") as f:
        insert_data_offer(json.load(f))
