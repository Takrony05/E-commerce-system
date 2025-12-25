import sqlite3

class CartManager:
    def __init__(self, db_path="ecommerce.db"):
        self.db_path = db_path

    def connect(self):
        conn = sqlite3.connect(self.db_path)
        #conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def get_or_create_cart(self, user_id):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT cart_id FROM Cart WHERE user_id = ?",
            (user_id,)
        )
        result = cursor.fetchone()

        if result:
            cart_id = result[0]
        else:
            cursor.execute(
                "INSERT INTO Cart (user_id) VALUES (?)",
                (user_id,)
            )
            cart_id = cursor.lastrowid

        conn.commit()
        conn.close()
        return cart_id

    def add_to_cart(self, user_id, montag_id):
        conn = self.connect()
        cursor = conn.cursor()

        cart_id = self.get_or_create_cart(user_id)

        cursor.execute("""
            SELECT quantity FROM CartItems
            WHERE cart_id = ? AND product_id = ?
        """, (cart_id, montag_id))

        item = cursor.fetchone()

        if item:
            cursor.execute("""
                UPDATE CartItems
                SET quantity = quantity + 1
                WHERE cart_id = ? AND product_id = ?
            """, (cart_id, montag_id))
        else:
            cursor.execute("""
                INSERT INTO CartItems (cart_id, product_id, quantity)
                VALUES (?, ?, 1)
            """, (cart_id, montag_id))

        conn.commit()
        conn.close()
    

    def get_cart_items(self, cart_id):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                Products.product_id,
                Products.name,
                Products.price,
                CartItems.quantity,
                Products.image_path
            FROM CartItems
            JOIN Products ON Products.product_id = CartItems.product_id
            WHERE CartItems.cart_id = ?
        """, (cart_id,))

        items = cursor.fetchall()
        conn.close()
        return items

    
    def update_quantity(self, cart_id, product_id, quantity):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE CartItems
            SET quantity = ?
            WHERE cart_id = ? AND product_id = ?
        """, (quantity, cart_id, product_id))
        conn.commit()
        conn.close()

    def remove_item(self, cart_id, product_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM CartItems
            WHERE cart_id = ? AND product_id = ?
        """, (cart_id, product_id))
        conn.commit()
        conn.close()

    def remove_all_item(self, cart_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM CartItems
            WHERE cart_id = ?
        """, (cart_id,))
        conn.commit()
        conn.close()
