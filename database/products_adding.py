import sqlite3

class Product:
    def __init__(self, name, description, price, category_id, seller_id,image_Path):
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id
        self.seller_id = seller_id
        self.image_path = image_Path

        
class ProductManager:
    def __init__(self):
        self.db_path = "D:\E-C\E-commerce-system\ecommerce.db"

    def connect(self):
        conn = sqlite3.connect(self.db_path)
        # conn.execute("PRAGMA foreign_keys = ON")
        return conn


    def add_product(self, product):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Products (name, description, price, category_id, seller_id , image_Path)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (product.name, product.description, product.price,product.category_id, product.seller_id , product.image_path))
        conn.commit()
        conn.close()


pro=Product("coffe" ,"great" ,2 ,2,2,"eee")

pro1 =ProductManager()
pro1.add_product(pro)
