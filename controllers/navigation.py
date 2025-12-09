from gui.login_gui import LoginApp
from gui.register_gui import RegisterApp


class AppController:
    def __init__(self):
        self.current_app = None

    def start_login(self):
        if self.current_app:
            self.current_app.root.destroy()

        self.current_app = LoginApp(
            open_register_callback=self.start_register
        )
        self.current_app.run()

    def start_register(self):
        if self.current_app:
            self.current_app.root.destroy()

        self.current_app = RegisterApp(
            open_login_callback=self.start_login
        )
        self.current_app.run()
