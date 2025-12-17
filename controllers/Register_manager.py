import sqlite3
import hashlib
from datetime import datetime 
from pathlib import Path
from utlis.path_helper import get_db_path


def register_user(name, email, plain_password, role_id=1):
    conn = sqlite3.connect(get_db_path())
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


def login_user(email, plain_password):
    conn = sqlite3.connect(get_db_path())
    c = conn.cursor()

    password_hash = hashlib.sha256(plain_password.encode()).hexdigest()

    c.execute("""
        SELECT user_id, name, email, role_id
        FROM Users
        WHERE email = ? AND password_hash = ?
        LIMIT 1
    """, (email, password_hash))

    user = c.fetchone()
    conn.close()
    status = False
    if user:
        status = True
        return {
            "user_id": user[0],
            "name": user[1],
            "email": user[2],
            "role_id": user[3]
        }

    return None 
