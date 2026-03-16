from database.db import get_connection


class EmployeeService:

    @staticmethod
    def get_all_employees():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employee")
        employees = cursor.fetchall()

        conn.close()

        return employees