class Product:
    def __init__(self, name, description, price, category_id, seller_id,image_Path):
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id
        self.seller_id = seller_id
        self.image_path = image_Path
        
class Role:
    def __init__(self, role_id, role_name):
        self.role_id = role_id
        self.role_name = role_name

class User:
    def __init__(self, user_id, name, email, password_hash, role_id, created_at=None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.role_id = role_id
        self.created_at = created_at

class Category:
    def __init__(self, category_id, name, description=None):
        self.category_id = category_id
        self.name = name
        self.description = description


class Cart:
    def __init__(self, cart_id, user_id, created_at=None):
        self.cart_id = cart_id
        self.user_id = user_id
        self.created_at = created_at
        self.items = []  

class CartItem:
    def __init__(self, cart_item_id, cart_id, product_id, quantity):
        self.cart_item_id = cart_item_id
        self.cart_id = cart_id
        self.product_id = product_id
        self.quantity = quantity

class Order:
    def __init__(self, order_id, user_id, status, total_amount, order_date=None):
        self.order_id = order_id
        self.user_id = user_id
        self.status = status
        self.total_amount = total_amount
        self.order_date = order_date
        self.items = []  # list of OrderItem

class OrderItem:
    def __init__(self, order_item_id, order_id, product_id, quantity, price):
        self.order_item_id = order_item_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

class Shipping:
    def __init__(self, shipping_id, order_id, address, city, country, postal_code=None, status=None):
        self.shipping_id = shipping_id
        self.order_id = order_id
        self.address = address
        self.city = city
        self.country = country
        self.postal_code = postal_code
        self.status = status

class Payment:
    def __init__(self, payment_id, order_id, method, amount, payment_date=None):
        self.payment_id = payment_id
        self.order_id = order_id
        self.method = method
        self.amount = amount
        self.payment_date = payment_date

class Review:
    def __init__(self, review_id, user_id, product_id, rating, review_text=None, created_at=None):
        self.review_id = review_id
        self.user_id = user_id
        self.product_id = product_id
        self.rating = rating
        self.review_text = review_text
        self.created_at = created_at

class Report:
    def __init__(self, report_id, report_type, value=None, generated_at=None):
        self.report_id = report_id
        self.report_type = report_type
        self.value = value
        self.generated_at = generated_at
