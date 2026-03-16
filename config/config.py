import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

DATABASE_PATH = os.path.join(BASE_DIR, "database", "store.db")
TEST_DATABASE_PATH = os.path.join(BASE_DIR,"database", "test_store.db")