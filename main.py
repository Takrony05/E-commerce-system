from controllers.navigation import AppController
from gui.login_gui import LoginApp

def open_register():
    print("Open Register Page")

if __name__ == "__main__":
    app = LoginApp(open_register_callback=open_register)
    app.run()
