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
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products")  # table name
    products = cursor.fetchall()

    conn.close()
    return products