from controllers.navigation import AppController

if __name__ == "__main__":
    app = AppController()
    app.start_login()

# معرفش اي واحده فيهم الصح
from gui.login import LoginApp

def open_register():
    print("Open Register Page")

if __name__ == "__main__":
    app = LoginApp(open_register_callback=open_register)
    app.run()
