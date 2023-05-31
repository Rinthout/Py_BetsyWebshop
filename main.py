__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
from datetime import datetime


# Search for products based on a term. 
# Searching for 'sweater' should yield all products that have the word 'sweater' in the name. 
# This search should be case-insensitive
def search(term):
    term = term.lower()
    query = Product.select().where(Product.name.contains(term) | Product.description.contains(term))
    if query:
        for product in query:
            print(f'\n * Yes! We have {product.quantity}x of "{term}" in stock! * ')
    else:
        print(f'\n * We don\'t have any products like: "{term}", please try again. * ')

# View the products of a given user.
def list_user_products(user_id):
    product_query=(Product.select().join(ProductOwner).join(User).where(ProductOwner.owner == user_id))
    user_query = User.select().where(User.id == user_id).get()
    username = user_query.name
    if product_query:
        print(f'\n * User "{username}" has the following products:... ')    
        for product in product_query:
            print(f'   ...{product.quantity}x of "{product.name}" * ')


# View all products for a given tag.
def list_products_per_tag(tag_id):
    product_query = (Product.select().join(ProductTag).join(Tag).where(ProductTag.tag == tag_id))
    tag_query = Tag.select().where(Tag.id == tag_id).get()
    tagname = tag_query.name
    if product_query:
        print(f'\n * Products found by tag: "{tagname}"... ')
        for product in product_query:
            print(f'   ..."{product.name}" *')


# Add a product to a user.
def add_product_to_user(product_id, user_id):
    product_query = Product.select().where(Product.id == product_id).get()
    user_query = User.select().where(User.id == user_id).get()
    product = product_query.name
    username = user_query.name
    ProductOwner.create(product=product_id, owner=user_id, quantity=1)
    if product_query:
        print(f'\n * "{product}" is added to "{username}"! *')


# Remove a product from a user.
def remove_product(product_id, user_id):
    product_query = Product.select().where(Product.id == product_id).get()
    user_query = User.select().where(User.id == user_id).get()
    productname = product_query.name
    username = user_query.name
    if product_query:
        print(f'\n * "{productname}" from "{username}" is deleted *')
        product_query.delete_instance()


# Update the stock quantity of a product.
def update_stock(product_id, add_quantity):
    query = Product.select().where(Product.id == product_id).get()
    previous_quantity = query.quantity
    query.quantity = previous_quantity + add_quantity
    query.save()
    if query:
        print(f'\n * The stock for "{query.name}" is updated by "{add_quantity}". Updated stock is: "{query.quantity}" *')


# Handle a purchase between a buyer and a seller for a given product
def purchase_product(product_id, buyer_id, quantity):
    product_query = Product.select().where(Product.id == product_id).get()
    buyer_query = User.select().where(User.id == buyer_id).get()
    if quantity >= product_query.quantity:
        print(f'\n * Not enough of "{product_query.name}" on stock for transaction. Please enter new quantity less then "{product_query.quantity}" *')
        return

    total_price = round(product_query.price * quantity, 2)
   

    transactions = PurchaseTransaction.create(
        buyer = buyer_query.id,
        product_bought = product_query.id,
        qty_bought = quantity,
        total_price = total_price,
        date_bought = datetime.now()
    )
    
    new_quantity = product_query.quantity - quantity
    update_stock(product_query.id, new_quantity)

    print(f'\n * "{buyer_query.name}" bought "{transactions.qty_bought}"x of "{product_query.name}" *')
    print("=" * 40)
    print(
f'''ORDER TRANSACTION
    
\tPRODUCT:{product_query.name}
\tQUANTITY:{transactions.qty_bought}
    
\tPRICE:{transactions.total_price}
    
DATE:{str(transactions.date_bought)}''')
    print("=" * 40)

# Runs:
search("sweater")
search("jeanss")

list_user_products(2)

list_products_per_tag(2)

add_product_to_user(1,3)

update_stock(1, 200)

remove_product(3, 3)
               
purchase_product(2, 2, 100)

