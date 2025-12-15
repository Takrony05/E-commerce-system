import sqlite3
from models.product import Product, Category
from utlis.path_helper import get_db_path

class ProductManager:
    def __init__(self):
        self.db_path = get_db_path()

    def connect(self):
        conn = sqlite3.connect(self.db_path)
        # conn.execute("PRAGMA foreign_keys = ON")
        return conn
    
    def get_all_products(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [Product(*row) for row in rows]

    def get_product_by_id(self, product_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products WHERE id = ?", (product_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Product(*row)
        return None

    def update_product(self, product: Product):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Products
            SET name = ?, description = ?, price = ?, stock = ?, category_id = ?, seller_id = ?
            WHERE id = ?
        """, (product.name, product.description, product.price, product.stock, product.category_id, product.seller_id, product.id))
        conn.commit()
        conn.close()

    def delete_product(self, product_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM Products WHERE product_id ={product_id}")
        conn.commit()
        conn.close()

    def search_products(self, name=None, category_id=None, price_range=None):
        conn = self.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM Products WHERE 1=1"
        params = []

        if name:
            query += " AND name LIKE ?"
            params.append(f"%{name}%")
        if category_id:
            query += " AND category_id = ?"
            params.append(category_id)
        if price_range:
            query += " AND price BETWEEN ? AND ?"
            params.extend(price_range)

        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()
        return [Product(*row) for row in rows]

    # -------------------------
    # Category functions
    # -------------------------
    def add_category(self, category: Category):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Categories (name) VALUES (?)", (category.name,))
        conn.commit()
        conn.close()

    def get_all_categories(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Categories")
        rows = cursor.fetchall()
        conn.close()
        return [Category(*row) for row in rows]

    def get_category_by_id(self, category_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Categories WHERE id = ?", (category_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Category(*row)
        return None

    def update_category(self, category: Category):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE Categories SET name = ? WHERE id = ?", (category.name, category.id))
        conn.commit()
        conn.close()

    def delete_category(self, category_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Categories WHERE id = ?", (category_id,))
        conn.commit()
        conn.close()
