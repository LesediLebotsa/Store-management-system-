
from models.Person import Person
from database.db import get_connection

class Employee(Person):
    def __init__(self, employee_id, name, surname, cell_number, email):
        super().__init__(employee_id, name, surname, cell_number, email)

    def insert(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO employee (employee_id, name, surname, cell_number, email)
            VALUES ( ?, ? ,? , ?, ?)  
        """, (
            # "?" are placeholders for employee details
            self.person_id,
            self.name,
            self.surname,
            self.cell_number,
            self.email
        ))

        conn.commit()
        conn.close()

        print("Employee added successfully")

    def remove(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM employees WHERE employee_id = ?",
            (self.person_id,)
        )

        conn.commit()
        conn.close()

        print("Employee removed successfully")

    def display_all(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employee")

        employee = cursor.fetchall()

        for emp in employee:
            print(emp)

        conn.close()




