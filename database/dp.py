import sqlite3
from database.path_helper import get_db_path

def initialize_database():
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()

    with open(get_db_path(), "r") as file:
        schema_sql = file.read()

    cursor.executescript(schema_sql)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully!")
