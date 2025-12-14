import sqlite3

def initialize_database():
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()

    with open(r"D:\E-C\E-commerce-system\database\schema.sql", "r") as file:
        schema_sql = file.read()

    cursor.executescript(schema_sql)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully!")
