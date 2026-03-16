# Store Management System API

## Overview

The **Store Management System API** is a backend application built with **Python and Flask** that manages store operations such as product inventory, employees, customers, and sales.

The project started as a **CLI-based school assignment** and was upgraded into a **modular backend API** following professional backend engineering practices.

The goal of this project is to demonstrate:

* Backend system architecture
* REST API design
* Database integration
* Automated testing
* Containerization

---

# Features

* Product inventory management
* Sales processing with automatic stock reduction
* Employee and customer management
* RESTful API endpoints
* Service layer architecture
* Structured logging
* Swagger API documentation
* Automated API tests with pytest
* Docker containerization

---

# Tech Stack

**Backend**

* Python
* Flask
* SQLite

**Architecture**

* Flask Blueprints
* Service Layer Pattern
* Modular project structure

**DevOps**

* Docker

**Testing**

* pytest
* Flask test client

**Documentation**

* Swagger / Flasgger

---

# Project Structure

store-management-system

config
└── config.py

database
├── db.py
└── store.db

interfaces
└── api
    ├── app.py
    └── routes
        ├── product_routes.py
        ├── employee_routes.py
        ├── customer_routes.py
        └── sales_routes.py

models
├── person.py
├── employee.py
├── customer.py
└── product.py

services
└── store_service.py

tests
├── test_products.py
└── test_sales.py

Dockerfile
requirements.txt
README.md

---

# Architecture

The system follows a **layered backend architecture**.

API Routes
↓
Service Layer (Business Logic)
↓
Database Layer (SQLite)

Responsibilities:

**Routes**

* Handle HTTP requests
* Validate input
* Return API responses

**Service Layer**

* Business logic
* Inventory updates
* Sales processing

**Database Layer**

* Persistent data storage

---

# API Endpoints

Products

GET /products
Retrieve all products

POST /products
Create a new product

PATCH /products/{id}/reduce
Reduce product inventory

Employees

GET /employees
Retrieve all employees

Customers

GET /customers
Retrieve all customers

Sales

POST /sales
Process a sale and update inventory

---

# API Documentation

Swagger documentation is available at:

http://localhost:5000/apidocs

This provides an interactive interface for exploring and testing API endpoints.

---

# Running the Application

## Local Development

Install dependencies:

pip install -r requirements.txt

Run the API:

python interfaces/api/app.py

API will be available at:

http://localhost:5000

---

# Running with Docker(Upcoming)

Build the image:

docker build -t store-api .

Run the container:

docker run -p 5000:5000 store-api

---

# Automated Testing

Run tests using pytest:

python -m pytest

Tests verify:

* product creation
* sales processing
* API response codes

---

# Future Improvements

Planned improvements include:

* Dedicated test database
* Docker containerization
* Improved validation and error handling
* Inventory protection logic
* API authentication
* CI/CD integration

---

# Learning Objectives

This project demonstrates practical experience with:

* Backend API development
* Service layer architecture
* Database integration
* Automated testing
* Containerization with Docker
* API documentation with Swagger

---

# Author

Lesedi Lebotsa
BSc IT (Software Engineering) Student
