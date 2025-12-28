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
        return [Product(row[0],row[1], row[2], row[3], row[4], row[5], row[6] , row[7]) for row in rows]

    def get_product_by_id(self, product_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products WHERE product_id = ?", (product_id,))
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
            WHERE product_id = ?
        """, (product.name, product.description, product.price, product.stock, product.category_id, product.seller_id, product.id))
        conn.commit()
        conn.close()

    def delete_product(self, product_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM Products WHERE product_id ={product_id}")
        conn.commit()
        conn.close()

    def search_products(self, category_id):
        with self.connect() as conn:
            cursor = conn.cursor()
            print(category_id)
            if category_id is None:
                cursor.execute("SELECT * FROM Products")
            else:
                cursor.execute("SELECT * FROM Products WHERE category_id = ?", (category_id,))
                
            return [Product(*row) for row in cursor.fetchall()]




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
