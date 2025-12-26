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
        ######################################################################### ADNAN
        Product("Coffe Shake", "Iced coffee", 20, 5, 1, "Coffe shake.jpg"),
        Product("V7 cola", "Egyptian Cola Drink", 25, 5, 1, "V7 cola.jpg"),
        Product("V7 pink lemonade", "Egyptian pink lemonade Drink", 25, 5, 1, "V7 pink lemonade.jpg"),
        Product("Friday Ice cream", "Vanilla ice cream", 15, 5, 1, "Friday icecream.jpg"),
        Product("Trident", "Gum", 2, 5, 1, "Trident.jpg"),
        Product("Bake Sticks", "Oven cooked sticks", 10, 5, 1, "Bake Sticks.jpg"),
        Product("balance", "Protein chips", 15, 5, 1, "balance.jpg"),
        Product("biskrem", "Cocoa Biscuits", 10, 5, 1, "biskrem.jpg"),
        Product("Water", "Mineral Water", 10, 5, 1, "Water.jpg"),
        Product("Domty Sandwich", "Filled sandwich", 15, 5, 1, "Domty.jpg"),
        Product("Doritos", "Tortilla chips", 10, 5, 1, "Doritos.jpg"),
        Product("Zabado", "Rayeb milk", 25, 5, 1, "zabado.jpg"),
        Product("Suntop", "Juice", 20, 5, 1, "suntop.jpg"),
        Product("Gummy Bears", "Gummy Bears", 30, 5, 1, "gummy bears.jpg"),
        Product("Molto", "filled croissant", 30, 5, 1, "molto.jpg"),
        Product("Snickers", "Chocolate with caramel and nuts", 35, 5, 1, "snickers.jpg"),
        Product("Twix", "Chocolate with biscuits and caramel", 35, 5, 1, "twix.jpg"),
        ####################################################################### Mohamed Ashraf
        Product("Gentian", "Gentian flower", 50, 1, 1, "Gentian flower.JPEG"),
        Product("Geranium", "Bright clustered blooms", 50, 1, 1, "Geranium.JPEG"),
        Product("Begonia", "waxy colorful petals", 50, 1, 1, "Begonia.JPEG"),
        Product("Celosia", "feathery flame-like", 50, 1, 1, "Celosia.JPEG"),
        Product("Roses", "classic romantic blooms", 50, 1, 1, "Roses.JPEG"),
        Product("Phlox", "dense fragrant clusters", 50, 1, 1, "Phlox.JPEG"),
        Product("Gladiolus", "tall elegant spikes", 50, 1, 1, "Gladiolus.JPEG"),
        Product("Flowers", "mixed garden flowers", 50, 1, 1, "Ward.JPEG"),
        Product("Amaryllis", "large trumpet flowers", 50, 1, 1, "Amaryllis.JPEG"),
        Product("Daisy", "simple cheerful petals", 50, 1, 1, "Daisy.JPEG"),
        Product("Daffodil", "bright yellow trumpet", 50, 1, 1, "Daffodil.JPEG"),
        Product("Lily", "elegant fragrant blooms", 50, 1, 1, "Lily.JPEG"),
        Product("Peony", "lush full petals", 50, 1, 1, "Peony.JPEG"),
        Product("Tulip", "smooth cup-shaped", 50, 1, 1, "Tulip.JPEG"),
        Product("Rose Garden", "layered rose petals", 50, 1, 1, "Rose Garden.JPEG"),

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