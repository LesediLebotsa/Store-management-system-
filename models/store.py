from database.db import get_connection
from services.logger import log_event

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_product(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
               INSERT INTO product (product_id, name, price, quantity)
               VALUES (?, ?, ?, ?)
           """, (
            self.product_id,
            self.name,
            self.price,
            self.quantity
        ))

        conn.commit()
        conn.close()

        print("Product added successfully")

    def remove_product(self, amount):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT quantity FROM products WHERE product_id = ?",
            (self.product_id,)
        )

        result = cursor.fetchone()

        if result is None:
            print("Product not found")
            conn.close()
            return

        current_quantity = result[0]

        if amount >= current_quantity:

            cursor.execute(
                "DELETE FROM products WHERE product_id = ?",
                (self.product_id,)
            )

            print("Product completely removed")

        else:

            cursor.execute(
                "UPDATE products SET quantity = quantity - ? WHERE product_id = ?",
                (amount, self.product_id)
            )

            print(f"{amount} units removed")

        conn.commit()
        conn.close()

    def display_products(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM product")

        product = cursor.fetchall()

        for prod in product:
            print(prod)

        conn.close()

    def update_product(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE product
            SET price = ?, quantity = ?
            WHERE product_id = ?
        """, (
            self.price,
            self.quantity,
            self.product_id
        ))

        conn.commit()
        conn.close()

        print("Product added successfully")

    def sell_product(self, quantity_sold):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT quantity FROM product WHERE product_id = ?",
            (self.product_id,)
        )

        result = cursor.fetchone()

        current_quantity = result[0]

        if quantity_sold > current_quantity:
            print("Not enough stock available")
            conn.close()
            return

        sales_total = self.price * quantity_sold

        cursor.execute("""
            UPDATE product
            SET quantity = quantity - ?
            WHERE product_id = ?
        """, (quantity_sold, self.product_id))

        cursor.execute("""
            INSERT INTO sales (date, product_name, sales_total)
            VALUES (DATE('now'), ?, ?)
        """, (
            self.name,
            sales_total
        ))
        log_event("SALE", f"Product: {self.name}, Quantity: {quantity_sold}, Total: {sales_total}")

        conn.commit()
        conn.close()

        print("Product sold successfully")
