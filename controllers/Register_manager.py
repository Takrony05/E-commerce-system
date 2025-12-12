import sqlite3
import hashlib
from datetime import datetime 
from pathlib import Path


def register_user(name, email, plain_password, role_id=1):
    conn = sqlite3.connect(r"c:\Users\omar sayed\Desktop\E-Commerce\ecommerce.db")
    c = conn.cursor()

    c.execute("SELECT 1 FROM Users WHERE email = ? LIMIT 1", (email,))
    exist = c.fetchone()
    if exist:
        conn.close()
        print("Email already exists")
        return False
         
    password_hash = hashlib.sha256(plain_password.encode()).hexdigest()

    sql_query = """
        INSERT INTO Users (name, email, password_hash, role_id) 
        VALUES (?, ?, ?, ?)
    """

    c.execute(sql_query, (name, email, password_hash, role_id))
    conn.commit()
    return True