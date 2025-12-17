import sqlite3
from utlis.path_helper import get_db_path

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
        self.db_path = get_db_path()

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

    products = [
        Product("Coffee", "Great coffee", 2, 2, 2, "download.jpg"),
        Product("Tea", "Refreshing tea", 1.5, 2, 2, "tea.jpg"),
        Product("Laptop", "High performance laptop", 1200, 1, 1, "laptop.jpg"),
        Product("Smartphone", "Latest model smartphone", 800, 1, 1, "smartphone.jpg"),
        Product("Headphones", "Noise-cancelling headphones", 150, 3, 1, "headphones.jpg"),
        Product("Camera", "Digital SLR camera", 500, 1, 1, "camera.jpg"),
        Product("Book", "Bestselling novel", 20, 4, 3, "book.jpg"),
        Product("Desk Lamp", "LED desk lamp", 30, 5, 2, "desklamp.jpg"),
    ]

    def add_all_products(self):
        conn = self.connect()
        cursor = conn.cursor()
        
        product_data = [
            (p.name, p.description, p.price, p.category_id, p.seller_id, p.image_path)
            for p in self.products
        ]
        
        cursor.executemany("""
            INSERT INTO Products (name, description, price, category_id, seller_id, image_Path)
            VALUES (?, ?, ?, ?, ?, ?)
        """, product_data)
        
        conn.commit()
        conn.close()