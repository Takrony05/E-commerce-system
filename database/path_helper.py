import os
import sqlite3

def get_db_path(db_filename="ecommerce.db"):
    utils_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.normpath(os.path.join(utils_dir, ".."))
    db_path = os.path.join(project_root, db_filename)
    return db_path

def get_schema_path(db_filename="schema.sql"):
    utils_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.normpath(os.path.join(utils_dir, ".."))
    schema_path = os.path.join(project_root, db_filename)
    return schema_path

def fetch_products():
    conn = sqlite3.connect(get_db_path())
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    conn.close()
    return products