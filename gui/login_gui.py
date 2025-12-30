import customtkinter as ctk
from PIL import Image, ImageTk
from pathlib import Path
from gui.products import ProductsUI
from gui.shop import ShopsUI
from controllers.Register_manager import login_user
from tkinter import messagebox
from utlis.path_helper import get_image_path as gip
ctk.set_appearance_mode("light")

class LoginApp:
    def __init__(self, open_register_callback):
        self.open_register_callback = open_register_callback
        self.root = ctk.CTk()
        self.root.title("E-JUST Store - Login")
        self.root.after(0, lambda: self.root.state("zoomed"))
        self.root.state("zoomed")
        self.root.configure(fg_color="#f5f5f5")
        self.root.iconbitmap(gip("icon.ico"))
        self.setup_ui()
    
    def setup_ui(self):
        
        base_path = Path(__file__).resolve().parent
        bg_path = base_path / "assets" / "background1.jpg"

        if bg_path.exists():
            bg_image_pil = Image.open(bg_path) 
            
            
            self.bg_ctk_image = ctk.CTkImage(
                light_image=bg_image_pil, 
                dark_image=bg_image_pil,
                size=(self.root.winfo_screenwidth(), self.root.winfo_screenheight()) 
            )

            bg_label = ctk.CTkLabel(self.root, image=self.bg_ctk_image, text="")
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            bg_label.lower()

        else:
            print(f"Error: Background file not found at {bg_path}")
        # ---------------- Title Bar ----------------
        title_frame = ctk.CTkFrame(
            self.root,
            fg_color="#c0392b",
            height=110,
            corner_radius=0
        )
        title_frame.place(x=0, y=0, relwidth=1)
        title_frame.pack_propagate(False)

        ctk.CTkLabel(
            title_frame,
            text="JUST E-BUY  ",
            font=ctk.CTkFont(
                family="Comic Sans MS",
                size=56,
                weight="bold",
                slant="italic"
            ),
            text_color="white"
        ).place(relx=0.5, rely=0.5, anchor="center")

        
        self.login_frame = ctk.CTkFrame(
            self.root,
            width=370,
            height=440,
            fg_color="white",
            corner_radius=25,
            border_width=4,
            border_color="#c0392b"
        )

        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.login_frame.pack_propagate(False)

        #login
        ctk.CTkLabel(
            self.login_frame,
            text="SIGN IN",
            font=ctk.CTkFont("Arial Black", 38),
            text_color="#2c3e50"
        ).pack(pady=(35, 28))

        # ---------------- Entries ----------------
        entry_style = {
            "width": 280,
            "height": 42,
            "corner_radius": 16,
            "font": ctk.CTkFont(size=15),
            "fg_color": "white",
            "border_width": 2,
            "border_color": "#c0392b",
            "text_color": "#2c3e50",
            "placeholder_text_color": "#95a5a6"
        }

        self.acc_entry = ctk.CTkEntry(
            self.login_frame,
            placeholder_text="Enter your e-mail",
            **entry_style
        )
        self.acc_entry.pack(pady=(5, 18))

        self.pass_entry = ctk.CTkEntry(
            self.login_frame,
            placeholder_text="Enter your password",
            show="*",
            **entry_style
        )
        self.pass_entry.pack(pady=(0, 30))
        self.pass_entry.bind("<Return>", lambda event: self.login_action())


        # ---------------- Register Button ----------------
        ctk.CTkButton(
        self.login_frame,
        text="REGISTER",
        width=130,
        height=38,
        corner_radius=20,
        fg_color="#eeeeee",
        hover_color="#cfcfcf",
        text_color="#7f8c8d",
        font=ctk.CTkFont(weight="bold"),
        command=self.go_to_register
    ).pack(pady=(0, 25))
    


        ctk.CTkButton(
            self.login_frame,
            text="SIGN IN",
            width=300,
            height=60,
            corner_radius=32,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="white",
            command=self.login_action
        ).pack(pady=(10, 20))

    def go_to_register(self):
        self.open_register_callback()
    
    def login_action(self):
        email = self.acc_entry.get().strip().lower()
        password = self.pass_entry.get()

        if not email or not password:
            messagebox.showerror(title="Error", message="Please enter email and password")
            return

        user = login_user(email, password)

        if not user:
            messagebox.showerror(
                title="Log in Failed",
                message="Invalid email or password"
            )
            return

        
        self.root.destroy()

        app = ShopsUI(user)   
        app.run()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = LoginApp()
    app.run()

# if __name__ == "__main__":
#     def dummy_register():
#         print("Register button clicked (dummy)")

#     app = LoginApp(open_register_callback=dummy_register)
#     app.run()
