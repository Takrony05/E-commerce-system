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
        Product("Coffe Shake", "Iced coffee", 20, 5, 1, "Coffe shake.jpg"),
        Product("V7 cola", "Egyptian Cola Drink", 25, 5, 1, "V7 cola.jpg"),
        Product("V7 pink lemonade", "Egyptian pink lemonade Drink", 25, 5, 1, "V7 pink.png"),
        Product("Friday Ice cream", "Vanilla ice cream", 15, 5, 1, "Friday icecream.jpg"),
        Product("Trident", "Gum", 2, 5, 1, "Trident.jpg"),
        Product("Bake Sticks", "Oven cooked sticks", 10, 5, 1, "Bake Sticks.jpg"),
        Product("balance", "Protein chips", 15, 5, 1, "balance.jpg"),
        Product("biskrem", "Cocoa Biscuits", 10, 5, 1, "biskrem.jpg"),
        Product("Water", "Mineral Water", 10, 5, 1, "Water.jpeg"),
        Product("Domty Sandwich", "Filled sandwich", 15, 5, 1, "Domty.jpg"),
        Product("Doritos", "Tortilla chips", 10, 5, 1, "Doritos.jpg"),
        Product("Zabado", "Rayeb milk", 25, 5, 1, "zabado.jpg"),
        Product("Suntop", "Juice", 20, 5, 1, "suntop.jpg"),
        Product("Gummy Bears", "Gummy Bears", 30, 5, 1, "gummy bears.jpg"),
        Product("Molto", "filled croissant", 30, 5, 1, "molto.jpeg"),
        Product("Snickers", "Chocolate with caramel and nuts", 35, 5, 1, "snikers.jpg"),
        Product("Twix", "Chocolate with biscuits and caramel", 35, 5, 1, "twix.jpg"),
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
        Product("Rose Garden", "layered rose petals", 50, 1, 1, "Rose Garden.jpg"),
        Product("Poinsettia", "festive red bracts", 50, 1, 1, "Poinsettia.JPEG"),
        Product("Monkshood", "tall hooded blooms", 50, 1, 1, "Monkshood.JPEG"),
        Product("Mokara Orchid", "vibrant exotic orchid", 50, 1, 1, "Mokara Orchid.JPEG"),
        Product("Liatris", "purple fuzzy spikes", 50, 1, 1, "Liatris.JPEG"),
        Product("Hydrangea", "large rounded clusters", 50, 1, 1, "Hydrangea.JPEG"),
        Product("Pink Blooms", "soft pink blooms", 50, 1, 1, "Pink tany.JPEG"),
        Product("Heather", "tiny clustered flowers", 50, 1, 1, "Heather.JPEG"),
        Product("Garbera", "bold daisy-like", 50, 1, 1, "Garbera.JPEG"),
        Product("Orchid", "delicate exotic blooms", 50, 1, 1, "Orchid.JPEG"),
        Product("Dahlia", "intricate layered petals", 50, 1, 1, "Dahlia.JPEG"),
        Product("Cosmos", "airy delicate petals", 50, 1, 1, "Cosmos.JPEG"),
        Product("Pink Pastels", "soft pastel blooms", 50, 1, 1, "pink.JPEG"),
        Product("Carnation Mini", "small ruffled flowers", 50, 1, 1, "Carnation Mini.JPEG"),
        Product("Carnation", "frilled long-lasting", 50, 1, 1, "Carnation.JPEG"),
        Product("Gypsophila", "tiny white sprays", 50, 1, 1, "Gypsophila.JPEG"),
        Product("Alstroemeria", "spotted lily-like", 50, 1, 1, "Alstroemeria.JPEG"),
        Product("Allium", "spherical purple globe", 50, 1, 1, "Allium.JPEG"),
        Product("Agapanthus", "blue star clusters", 50, 1, 1, "Agapanthus.JPEG"),
        Product("Achillea yellow", "flat yellow clusters", 50, 1, 1, "Achilleayellow.JPEG"),
        Product("Achillea", "flat-topped blooms", 50, 1, 1, "Achillea.JPEG"),
        Product("Acacia", "fluffy yellow balls", 50, 1, 1, "Acacia.JPEG"),
        Product("Bluebells", "drooping blue bells", 50, 1, 1, "Bluebells.JPEG"),
        Product("Wallet", "compact leather holder", 50, 2, 1, "wallet.jpg"),
        Product("Mug", "ceramic coffee mug", 50, 2, 1, "Mug.JPEG"),
        Product("Purse", "slim zip pouch", 50, 2, 1, "purse.jpg"),
        Product("Bear", "soft plush toy", 50, 2, 1, "bearq.jpg"),
        Product("Keychain", "small decorative keys", 50, 2, 1, "keychain.jpg"),
        Product("Cap", "casual sports cap", 50, 2, 1, "Cap.JPEG"),
        Product("EJUST T-shirt", "cotton shirt with EJUST written on it", 50, 2, 1, "EJUST tshirt.jpg"),
        Product("Ring", "elegant gemstone ring", 50, 2, 1, "ring.jpg"),
        Product("Necklace", "delicate silver chain", 50, 2, 1, "necklace.jpg"),
        Product("Box", "decorative gift box", 50, 2, 1, "Box.jpg"),        
        Product("Nescafe", "Warm caffeine", 25, 4, 1, "Nescafe.jpg"),
        Product("Latte", "Espresso with Skimmed milk", 30, 4, 1, "Latte.jpg"),
        Product("Mocha", "Espresso with Chocolate", 30, 4, 1, "Mocha.jpg"),
        Product("Hot Chocolate", "Hot cocoa", 30, 4, 1, "Hot Chocolate.jpg"),
        Product("Water", "Mineral Water", 10, 4, 1, "Water.JPEG"),
        Product("V7 cola", "Egyptian Cola Drink", 25, 4, 1, "V7 cola.jpg"),
        Product("Square Pizza", "Warm Pizza", 15, 4, 1, "Square Pizza.jpg"),
        Product("pâté", "french pastery", 15, 4, 1, "pâté.jpg"),
        Product("Anise", "Anise Tea", 15, 4, 1, "Anise.jpg"),
        Product("Tea", "Black Tea", 15, 4, 1, "Tea.jpg"),
        Product("Milk Tea", "Tea with milk", 20, 4, 1, "Milk Tea.jpg"),
        Product("Fries Sandwich", "French Fries Sandwich", 30, 4, 1, "Fries Sandwich.jpg"),
        Product("Chicken Strips Sandwich", "Fried Strips Sandwich", 35, 4, 1, "Chicken Strips.jpg"),
        Product("Nescafe", "Warm caffeine", 25, 3, 1, "Nescafe.jpg"),
        Product("Latte", "Espresso with Skimmed milk", 30, 3, 1, "Latte.jpg"),
        Product("Mocha", "Espresso with Chocolate", 30, 3, 1, "Mocha.jpg"),
        Product("Tea", "Black Tea", 15, 3, 1, "Tea.jpg"),
        Product("Milk Tea", "Tea with milk", 20, 3, 1, "Milk Tea.jpg"),
        Product("Turkish Coffee", "Classic Coffee", 20, 3, 1, "Turkish Coffee.jpg"),
        Product("French Coffee", "Coffee with milk", 25, 3, 1, "French Coffee.jpg"),
        Product("Anise", "Anise Tea", 15, 3, 1, "Anise.jpg"),
        Product("Spanish Latte", "Espresso With condensed milk", 50, 3, 1, "Spanish Latte.jpg"),
        Product("Vanilla Milk Shake", "Cold vanilla shake", 40, 3, 1, "Vanilla MilkShake.jpg"),
        Product("Chocolate Milk Shake", "Cold chocolate shake", 40, 3, 1, "Chocolate MilkShake.jpg"),
        Product("Indomie", "Instant Noodles", 15, 3, 1, "Indomie.jpg"),
        Product("Hot Chocolate", "Hot cocoa", 30, 3, 1, "Hot Chocolate.jpg"),
        Product("Omar", "3am alnas", 1.75, 1, 1, "omar.jpeg"),
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