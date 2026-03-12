from models.Person import Person
from database.db import get_connection

class Customer(Person):
    def __init__(self, customer_id, name, surname, cell_number, email, billing_address):
        super().__init__(customer_id, name, surname, cell_number, email)
        self.billing_address = billing_address

    from database.db import get_connection

    def insert(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO customers (customer_id, name, surname, cell_number, email, billing_address)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            # ?'s are placeholders for customer information
            self.person_id,
            self.name,
            self.surname,
            self.cell_number,
            self.email,
            self.billing_address
        ))

        conn.commit()
        conn.close()

        print("Customer added successfully")

    def remove(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM customers WHERE customer_id = ?",
            (self.person_id,)
        )

        conn.commit()
        conn.close()

        print("Customer removed successfully")

    def display_all(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM customers")

        customers = cursor.fetchall()

        for cust in customers:
            print(cust)



        conn.close()
