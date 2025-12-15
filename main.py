from controllers.navigation import AppController
from gui.login_gui import LoginApp
from database.products_adding import ProductManager, Product
def open_register():
    print("Open Register Page")

if __name__ == "__main__":
    
    pro =ProductManager()
    pro.add_all_products()


    app = LoginApp(open_register_callback=open_register)
    app.run()
