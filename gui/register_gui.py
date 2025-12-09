import customtkinter as ctk
from PIL import Image, ImageTk
from pathlib import Path

ctk.set_appearance_mode("light")

class RegisterApp:
    def __init__(self, open_login_callback):
        self.open_login_callback = open_login_callback
        self.root = ctk.CTk()
        self.root.title("E-JUST Store - Register")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        self.setup_background()
        self.setup_ui()

    def setup_background(self):

        # ---------------- Background ----------------
        base_path = Path(__file__).resolve().parent
        bg_path = base_path / "assets" / "background.jpg"

        if bg_path.exists():
            bg_image_pil = Image.open(bg_path) 
            bg_image_pil = bg_image_pil.resize((900, 600), Image.Resampling.LANCZOS)
            
            self.bg_ctk_image = ctk.CTkImage(
                light_image=bg_image_pil, 
                dark_image=bg_image_pil,
                size=(900, 600) 
            )

            bg_label = ctk.CTkLabel(self.root, image=self.bg_ctk_image, text="")
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            bg_label.lower()

        else:
            print(f"Error: Background file not found at {bg_path}")

    def setup_ui(self):
        # الشريط الأحمر
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
            text="JUST E-pay  ",
            font=ctk.CTkFont(
                family="Comic Sans MS",
                size=56,
                weight="bold",
                slant="italic"
            ),
            text_color="white"
        ).place(relx=0.5, rely=0.5, anchor="center")

        # الصندوق الأبيض (مرفوع لفوق سنة)
        self.register_frame = ctk.CTkFrame(
            self.root,
            width=520,
            height=420,
            fg_color="white",
            corner_radius=28,
            border_width=5,
            border_color="#e74c3c"
        )
        self.register_frame.place(relx=0.5, rely=0.57, anchor="center")
        self.register_frame.pack_propagate(False)

        # عنوان REGISTER
        ctk.CTkLabel(
            self.register_frame,
            text="REGISTER",
            font=ctk.CTkFont("Arial Black", 38),
            text_color="#2c3e50"
        ).pack(pady=(30, 20))

        entry_style = {
            "width": 300,
            "height": 45,
            "corner_radius": 20,
            "fg_color": "white",
            "border_width": 3,
            "border_color": "#e74c3c",
            "font": ctk.CTkFont(size=16),
            "placeholder_text_color": "#95a5a6",
            "text_color": "#2c3e50"
        }

        self.acc_entry = ctk.CTkEntry(
            self.register_frame,
            placeholder_text="Enter your account",
            **entry_style
        )
        self.acc_entry.pack(pady=12)

        self.pass_entry = ctk.CTkEntry(
            self.register_frame,
            placeholder_text="Enter your password",
            show="*",
            **entry_style
        )
        self.pass_entry.pack(pady=12)

        self.confirm_entry = ctk.CTkEntry(
            self.register_frame,
            placeholder_text="Confirm password",
            show="*",
            **entry_style
        )
        self.confirm_entry.pack(pady=(12, 30))

        # زرار SIGN UP
        ctk.CTkButton(
            self.register_frame,
            text="SIGN UP",
            width=240,
            height=55,
            corner_radius=35,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color="white",
            command=self.signup_action
        ).pack()

    def signup_action(self):
        print("Account:", self.acc_entry.get())
        print("Password:", self.pass_entry.get())
        print("Confirm:", self.confirm_entry.get())

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = RegisterApp()
    app.run()
