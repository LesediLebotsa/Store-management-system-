from database.db import get_connection

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

    def remove_product(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM product WHERE product_id = ?",
            (self.product_id,)
        )

        conn.commit()
        conn.close()

        print("Product was removed successfully")

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

        conn.commit()
        conn.close()

        print("Product sold successfully")