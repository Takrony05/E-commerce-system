import customtkinter as ctk
from PIL import Image
from pathlib import Path

ctk.set_appearance_mode("light")


class CartUI:
    def __init__(self, cart_items: list):
        self.cart_items = cart_items

        self.root = ctk.CTk()
        self.root.title("E-JUST Store | Cart")
        self.root.geometry("1100x700")
        self.root.resizable(False, False)
        self.root.configure(fg_color="#f5f5f5")

        self.setup_ui()

    # ================= MAIN UI =================

    def setup_ui(self):
        self.setup_background()
        self.setup_title()
        self.setup_main_container()

    def setup_background(self):
        base_path = Path(__file__).resolve().parent
        bg_path = base_path / "assets" / "background.jpg"

        if bg_path.exists():
            img = Image.open(bg_path).resize((1100, 700))
            self.bg_image = ctk.CTkImage(img, img, size=(1100, 700))
            lbl = ctk.CTkLabel(self.root, image=self.bg_image, text="")
            lbl.place(x=0, y=0, relwidth=1, relheight=1)
            lbl.lower()

    def setup_title(self):
        title = ctk.CTkFrame(
            self.root,
            height=100,
            fg_color="#c0392b",
            corner_radius=0
        )
        title.place(x=0, y=0, relwidth=1)
        title.pack_propagate(False)

        ctk.CTkLabel(
            title,
            text="JUST E-Buy  |  Shopping Cart",
            font=ctk.CTkFont(
                family="Comic Sans MS",
                size=40,
                weight="bold",
                slant="italic"
            ),
            text_color="white"
        ).place(relx=0.5, rely=0.5, anchor="center")

    def setup_main_container(self):
        main = ctk.CTkFrame(
            self.root,
            width=1000,
            height=560,
            fg_color="white",
            corner_radius=25,
            border_width=4,
            border_color="#c0392b"
        )
        main.place(relx=0.5, rely=0.57, anchor="center")
        main.pack_propagate(False)

        self.cart_area = ctk.CTkScrollableFrame(
            main,
            width=650,
            height=520,
            fg_color="white"
        )
        self.cart_area.place(x=20, y=20)

        self.summary_area = ctk.CTkFrame(
            main,
            width=280,
            height=520,
            fg_color="#fafafa",
            corner_radius=20,
            border_width=2,
            border_color="#c0392b"
        )
        self.summary_area.place(x=700, y=20)
        self.summary_area.pack_propagate(False)

        self.render_cart_items()
        self.render_summary()

    # المشتريات

    def render_cart_items(self):
        for widget in self.cart_area.winfo_children():
            widget.destroy()

        if not self.cart_items:
            ctk.CTkLabel(
                self.cart_area,
                text="Your cart is empty",
                font=ctk.CTkFont(size=18, weight="bold"),
                text_color="#7f8c8d"
            ).pack(pady=200)
            return

        for item in self.cart_items:
            self.create_cart_row(item)

    def create_cart_row(self, item):
        row = ctk.CTkFrame(
            self.cart_area,
            height=90,
            fg_color="white",
            corner_radius=15,
            border_width=1,
            border_color="#e0e0e0"
        )
        row.pack(fill="x", pady=8)
        row.pack_propagate(False)

        ROW_Y = 35  # unified horizontal line # ana msh AI #

        # صور المنتج
        img_path = Path(item["image_path"])
        if img_path.exists():
            img = Image.open(img_path).resize((70, 70))
            img_ctk = ctk.CTkImage(img, img, size=(70, 70))
            lbl = ctk.CTkLabel(row, image=img_ctk, text="")
            lbl.image = img_ctk
            lbl.place(x=10, y=10)

        # الاسم 
        ctk.CTkLabel(
            row,
            text=item["name"],
            font=ctk.CTkFont(weight="bold")
        ).place(x=90, y=22)

        # السعؤ
        ctk.CTkLabel(
            row,
            text=f"{item['price']} EGP",
            text_color="#7f8c8d"
        ).place(x=90, y=46)

        # qantity 
        qty_frame = ctk.CTkFrame(row, fg_color="transparent")
        qty_frame.place(x=350, y=ROW_Y - 15)

        ctk.CTkButton(
            qty_frame,
            text="-",
            width=30,
            height=30,
            command=lambda i=item: self.update_quantity(i, -1)
        ).pack(side="left", padx=4)

        ctk.CTkLabel(
            qty_frame,
            text=str(item["quantity"]),
            width=40,
            anchor="center",
            font=ctk.CTkFont(weight="bold")
        ).pack(side="left")

        ctk.CTkButton(
            qty_frame,
            text="+",
            width=30,
            height=30,
            command=lambda i=item: self.update_quantity(i, 1)
        ).pack(side="left", padx=4)

        # ---------- Total ----------
        total = item["price"] * item["quantity"]
        ctk.CTkLabel(
            row,
            text=f"{total} EGP",
            font=ctk.CTkFont(weight="bold"),
            text_color="#c0392b"
        ).place(x=520, y=ROW_Y)

    def update_quantity(self, item, delta):
        item["quantity"] = max(0, item["quantity"] + delta)
        self.render_cart_items()
        self.render_summary()

    # paymint

    def render_summary(self):
        for widget in self.summary_area.winfo_children():
            widget.destroy()

        ctk.CTkLabel(
            self.summary_area,
            text="paymint",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(pady=20)

        total = 0

        for item in self.cart_items:
            if item["quantity"] == 0:
                continue

            line_total = item["price"] * item["quantity"]
            total += line_total

            row = ctk.CTkFrame(self.summary_area, fg_color="transparent")
            row.pack(fill="x", padx=20, pady=5)

            ctk.CTkLabel(
                row,
                text=f"{item['name']} x{item['quantity']}"
            ).pack(side="left")

            ctk.CTkLabel(
                row,
                text=f"{line_total} EGP"
            ).pack(side="right")

        ctk.CTkFrame(
            self.summary_area,
            height=2,
            fg_color="#e0e0e0"
        ).pack(fill="x", padx=20, pady=15)

        ctk.CTkLabel(
            self.summary_area,
            text=f"Total: {total} EGP",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#c0392b"
        ).pack(pady=10)

        ctk.CTkButton(
            self.summary_area,
            text="Checkout Now",
            height=45,
            corner_radius=25,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            font=ctk.CTkFont(weight="bold")
        ).pack(padx=20, pady=20, fill="x")


    def run(self):
        self.root.mainloop()



