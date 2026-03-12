from models.employee import Employee
from models.customer import Customer
from models.store import Product

#EMPLOYEE MENU FUNCTIONS
#=======================================================================================
def employee_menu():

    while True:

        print("\n--- Employee Menu ---")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Display Employees")
        print("0. Back")

        choice = input("Select option: ")

        if choice == "1":

            emp_id = int(input("Employee ID: "))
            name = input("Name: ")
            surname = input("Surname: ")
            cell = input("Cell number: ")
            email = input("Email: ")

            emp = Employee(emp_id, name, surname, cell, email)
            emp.insert()

        elif choice == "2":

            emp_id = int(input("Employee ID to remove: "))
            emp = Employee(emp_id, "", "", "", "")
            emp.remove()

        elif choice == "3":

            emp = Employee(0, "", "", "", "")
            emp.display_all()

        elif choice == "0":
            break

        else:
            print("Invalid option")

#==========================================================================================
#CUSTOMER MENU FUNCTIONS

def customer_menu():

    while True:

        print("\n--- Customer Menu ---")
        print("1. Add Customer")
        print("2. Remove Customer")
        print("3. Display Customers")
        print("0. Back")

        choice = input("Select option: ")

        if choice == "1":

            cust_id = int(input("Customer ID: "))
            name = input("Name: ")
            surname = input("Surname: ")
            cell = input("Cell number: ")
            email = input("Email: ")
            address = input("Billing Address: ")

            cust = Customer(cust_id, name, surname, cell, email, address)
            cust.insert()

        elif choice == "2":

            cust_id = int(input("Customer ID to remove: "))
            cust = Customer(cust_id, "", "", "", "", "")
            cust.remove()

        elif choice == "3":

            cust = Customer(0, "", "", "", "", "")
            cust.display_all()

        elif choice == "0":
            break

        else:
            print("Invalid option")
#==================================================================================================
#PRODUCT MENU FUNCTIONS
def product_menu():

    while True:

        print("\n--- Product Menu ---")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Display Products")
        print("0. Back")

        choice = input("Select option: ")

        if choice == "1":

            product_id = int(input("Product ID: "))
            name = input("Product Name: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))

            p = Product(product_id, name, price, quantity)
            p.add_product()

        elif choice == "2":

            product_id = int(input("Product ID: "))
            price = float(input("New Price: "))
            quantity = int(input("New Quantity: "))

            p = Product(product_id, "", price, quantity)
            p.update_product()

        elif choice == "3":

            p = Product(0, "", 0, 0)
            p.display_products()

        elif choice == "0":
            break

        else:
            print("Invalid option")
#=============================================================================================
#SALES MENU FUNCTIONS
def sales_menu():

    while True:

        print("\n--- Sales Menu ---")
        print("1. Sell Product")
        print("0. Back")

        choice = input("Select option: ")

        if choice == "1":

            product_id = int(input("Product ID: "))
            name = input("Product Name: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity to sell: "))

            p = Product(product_id, name, price, 0)
            p.sell_product(quantity)

        elif choice == "0":
            break

        else:
            print("Invalid option")

#==================================================================================================
#MAIN MENU FUNCTIONS
def main_menu():
    while True:

        print("Welcome to the store Management System!")
        print("\n1. Manage Employees")
        print("2. Manage Customers")
        print("3. Manage Products")
        print("4. Manage Sales")
        print("0. Exit")

        choice = input("Please select an option: ")

        if choice == "1":
            employee_menu()
        elif choice == "2":
            customer_menu()
        elif choice == "3":
            product_menu()
        elif choice == "4":
            sales_menu()
        elif choice == "0":
            print("Exiting system")
            break
        else:
            print("Please select a valid option")


main_menu()
