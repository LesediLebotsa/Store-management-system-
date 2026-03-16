import sqlite3
from config.config import DATABASE_PATH
from flask import current_app

def get_connection(db_path=None):
    if db_path is None:
        db_path = DATABASE_PATH
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn
