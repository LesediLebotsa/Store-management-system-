# Store Management System

A Python-based **Store Management System** built using **Object-Oriented Programming (OOP)** and **SQLite**.
The system manages employees, customers, products, and sales while maintaining inventory records and logging transactions.

This project was originally developed as a coursework assignment and later upgraded into a **portfolio project demonstrating backend architecture, layered design, and software engineering practices.**

---

# Features

### Employee Management

* Add employees
* Remove employees
* Display employee records

### Customer Management

* Add customers
* Remove customers
* Display customer records

### Product Inventory

* Add products
* Update product price and quantity
* Remove products or reduce inventory when items are damaged
* Display available products

### Sales Processing

* Sell products
* Automatically update inventory after each sale
* Record sales transactions

### Logging System

All important system actions such as sales transactions are logged to a file.

Example log entry:

```
2026-03-13 10:11:02 | SALE | Product: Laptop | Quantity: 2 | Total: 2400
```

Logs are stored in:

```
logs/system_log.txt
```

This helps track system activity and demonstrates **basic production logging practices**.

### Input Validation

The system validates user inputs to prevent invalid data from entering the system.

Examples include:

* Preventing negative prices
* Ensuring product quantities are positive
* Validating product and employee IDs
* Preventing invalid menu selections

