from peewee import *

db = SqliteDatabase("betsy_webshop.db", pragmas={"foreign_keys": 1})


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = AutoField(unique=True)
    name = TextField()
    address = TextField()
    iban = TextField()


class Product(BaseModel):
    product_id = AutoField(unique=True)
    owner = ForeignKeyField(User, backref="products")
    name = TextField()
    description = TextField()
    price = DecimalField(decimal_places=2, auto_round=True)
    quantity = IntegerField()


class Transactions(BaseModel):
    transaction_id = AutoField(unique=True)
    buyer_id = ForeignKeyField(User, backref="purchases")
    product_id = ForeignKeyField(Product, backref="sales")
    quantity = IntegerField()


class Tag(BaseModel):
    tag_id = AutoField(unique=True)
    name = TextField(unique=True)


class ProductTag(BaseModel):
    product = ForeignKeyField(Product, backref="tags")
    tag = ForeignKeyField(Tag, backref="products")


