import os
import pytest
from interfaces.api.app import create_app
from config.config import TEST_DATABASE_PATH
from database.db import get_connection



@pytest.fixture
def client():
    app = create_app({
        "TESTING": True,
        "DATABASE": TEST_DATABASE_PATH
    })

    with app.test_client() as client:
        yield client


@pytest.fixture(autouse=True)
def setup_test_db():
    if os.path.exists(TEST_DATABASE_PATH):
        os.remove(TEST_DATABASE_PATH)

    conn = get_connection(TEST_DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL,
        quantity INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE sales (
        id INTEGER PRIMARY KEY,
        product_id INTEGER,
        quantity INTEGER
    )
    """)

    conn.commit()
    conn.close()

    yield

    if os.path.exists(TEST_DATABASE_PATH):
        os.remove(TEST_DATABASE_PATH)