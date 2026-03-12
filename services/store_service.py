from models.store import Product



def add_product(product_id, name, price, quantity):
    product = Product(product_id, name, price, quantity)
    product.add_product()


def update_product(product_id, price, quantity):
    product = Product(product_id, "", price, quantity)
    product.update_product()


def display_products():
    product = Product(0, "", 0, 0)
    product.display_products()


def sell_product(product_id, name, price, quantity):
    product = Product(product_id, name, price, 0)
    product.sell_product(quantity)

def remove_product(product_id, amount):
    product = Product(product_id, "", 0, 0)
    product.remove_product(amount)
