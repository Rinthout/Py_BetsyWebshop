import os
from models import *


def delete_database():
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "betsywebshop.db")
    if os.path.exists(database_path):
        os.remove(database_path)


def populate_test_database():

    db.connect()

    db.create_tables([User, Product, Tag, ProductTag, ProductOwner, PurchaseTransaction])

    users = [
        {"name": "Terry", "address": "Terrystreet", "iban": "1111"},
        {"name": "Graham", "address": "Grahamstreet", "iban": "2222"},
        {"name": "John", "address": "Johnstreet", "iban": "3333"},
        {"name": "Erica", "address": "Ericastreet", "iban": "4444"},
    ]

    for user in users:
        User.create(
            name=user["name"],
            address=user["address"],
            iban=user["iban"]
        )

    products = [
        {"name": "sweater", "description": "Men green sweater", "price": 75.00, "quantity": 30},
        {"name": "hoodie", "description": "Men blue hoodie", "price": 50.00, "quantity": 130},
        {"name": "jeans", "description": "Men grey jeans", "price": 115.00, "quantity": 50},
        {"name": "dress", "description": "Women printed dress", "price": 25.00, "quantity": 175},
        {"name": "sneakers", "description": "Women white sneakers", "price": 155.00, "quantity": 200},
        {"name": "jacket", "description": "Women black jacket", "price": 75.00, "quantity": 70},
    ]
    
    for product in products:
        Product.create(
            name=product["name"],
            description=product["description"],
            price=product["price"],
            quantity=product["quantity"],
        )

    tags = [
        {"name": "men"},
        {"name": "women"}
    ]
    
    for tag in tags:
        Tag.create(
            name=tag["name"]
        )

    product_tags = [
        {"product": 1, "tag": 1},
        {"product": 2, "tag": 1},
        {"product": 3, "tag": 1},
        {"product": 4, "tag": 2},
        {"product": 5, "tag": 2},
        {"product": 6, "tag": 2},
    ]

    for product_tag in product_tags:
        ProductTag.create(
            product=product_tag["product"],
            tag=product_tag["tag"]
        )

    product_owners = [
        {"product": 1, "owner": 4, "quantity": 2},
        {"product": 3, "owner": 3, "quantity": 4},
        {"product": 5, "owner": 2, "quantity": 6},
        {"product": 6, "owner": 1, "quantity": 8}
    ]

    for product_owner in product_owners:
        ProductOwner.create(
            product=product_owner["product"],
            owner=product_owner["owner"],
            quantity=product_owner["quantity"]
        )

    db.close()

delete_database()
populate_test_database()