import customtkinter as ctk
from PIL import Image, ImageTk
from pathlib import Path
from utlis.path_helper import get_db_path
from controllers.Register_manager import register_user
from tkinter import messagebox

ctk.set_appearance_mode("light")

class RegisterApp:
    def __init__(self, open_login_callback=None):
        self.open_login_callback = open_login_callback
        self.root = ctk.CTk()
        self.root.title("E-JUST Store - Register")
        self.root.after(0, lambda: self.root.state("zoomed"))
        self.root.state("zoomed")

        self.setup_background()
        self.setup_ui()

    def setup_background(self):
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

    def setup_ui(self):

        # العنوان
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
            text="JUST E-Buy",
            font=ctk.CTkFont(
                family="Comic Sans MS",
                size=56,
                weight="bold",
                slant="italic"
            ),
            text_color="white"
        ).place(relx=0.5, rely=0.5, anchor="center")

        # White Register Frame
        self.register_frame = ctk.CTkFrame(
            self.root,
            width=520,
            height=500,
            fg_color="white",
            corner_radius=28,
            border_width=5,
            border_color="#e74c3c"
        )
        self.register_frame.place(relx=0.5, rely=0.58, anchor="center")
        self.register_frame.pack_propagate(False)

        # REGISTER Title
        ctk.CTkLabel(
            self.register_frame,
            text="REGISTER",
            font=ctk.CTkFont("Arial Black", 38),
            text_color="#2c3e50"
        ).pack(pady=(25, 15))

        #Entry Style 
        entry_style = {
            "width": 320,
            "height": 50,
            "corner_radius": 20,
            "fg_color": "white",
            "border_width": 3,
            "border_color": "#e74c3c",
            "font": ctk.CTkFont(size=16),
            "placeholder_text_color": "#95a5a6",
            "text_color": "#2c3e50"
        }

        #الاسم
        self.name_entry = ctk.CTkEntry(
            self.register_frame,
            placeholder_text="Enter your name",
            **entry_style
        )
        self.name_entry.pack(pady=10)

        # الاكونت
        self.acc_entry = ctk.CTkEntry(
            self.register_frame,
            placeholder_text="Enter your e-mail",
            **entry_style
        )
        self.acc_entry.pack(pady=10)

        #الباسورد
        self.pass_entry = ctk.CTkEntry(
            self.register_frame,
            placeholder_text="Enter your password",
            show="*",
            **entry_style
        )
        self.pass_entry.pack(pady=10)

        # الباسووورد تاكيد 
        self.confirm_entry = ctk.CTkEntry(
            self.register_frame,
            placeholder_text="Confirm password",
            show="*",
            **entry_style
        )
        self.confirm_entry.pack(pady=(10, 25))

        # sign_up button
        ctk.CTkButton(
            self.register_frame,
            text="SIGN UP",
            width=250,
            height=60,
            corner_radius=35,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color="white",
            command=self.signup_action
        ).pack()

    def signup_action(self):
        customer_name = self.name_entry.get()             
        user_email = self.acc_entry.get() 
        password = self.pass_entry.get()
        confirm_password = self.confirm_entry.get()

        if not user_email or not password or not confirm_password or not customer_name:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return
        
        if user_email.count('@') != 1 or user_email.startswith('@') or user_email.endswith('@') or "@ejust.edu.eg" not in user_email:
            messagebox.showerror("Error", "Invalid email format.")
            return

        success = register_user(customer_name, user_email, password, role_id=1)
        
        if success == True:
            messagebox.showinfo("Success", "Account Added")
            self.acc_entry.delete(0, ctk.END)
            self.pass_entry.delete(0, ctk.END)
            self.confirm_entry.delete(0, ctk.END)
            self.name_entry.delete(0,ctk.END)

            if self.open_login_callback:
                self.open_login_callback()
    
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = RegisterApp()
    app.run()
