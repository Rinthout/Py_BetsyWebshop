from peewee import *

db = SqliteDatabase("betsywebshop.db")

class BaseModel(Model):

    class Meta:
        database = db

class User(BaseModel):
    name = CharField()
    address = CharField()
    iban = IntegerField()

class Product(BaseModel):
    name = CharField()
    description = TextField()
    price = DecimalField(decimal_places=2, auto_round=True)
    quantity = IntegerField()

class ProductOwner(BaseModel):
    product = ForeignKeyField(Product)
    owner = ForeignKeyField(User)
    quantity = IntegerField()

class Tag(BaseModel):
    name = CharField()

class ProductTag(BaseModel):
    product = ForeignKeyField(Product)
    tag = ForeignKeyField(Tag)

class PurchaseTransaction(BaseModel):
    buyer = ForeignKeyField(User)
    product_bought = ForeignKeyField(Product)
    qty_bought = IntegerField()
    total_price = DecimalField(decimal_places=2, auto_round=True)
    date_bought = DateTimeField(formats='%d-%m-%Y')

