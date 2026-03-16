import sqlite3
from config.config import DATABASE_PATH
print("using database:", DATABASE_PATH)
def get_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn
