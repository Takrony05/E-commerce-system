import customtkinter as ctk
from PIL import Image
from pathlib import Path
from database.path_helper import fetch_products

ctk.set_appearance_mode("light")


class ProductsUI:
    def __init__(self):
        self.products_list = fetch_products()

        self.root = ctk.CTk()
        self.root.title("E-JUST Store - Products")
        self.root.geometry("1100x700")
        self.root.resizable(False, False)
        self.root.configure(fg_color="#f5f5f5")

        self.setup_ui()

    def setup_ui(self):
        # ---------- Background ----------
        base_path = Path(__file__).resolve().parent
        bg_path = base_path / "assets" / "background.jpg"

        if bg_path.exists():
            bg_image = Image.open(bg_path).resize((1100, 700))
            self.bg_image = ctk.CTkImage(
                light_image=bg_image,
                dark_image=bg_image,
                size=(1100, 700)
            )
            bg_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            bg_label.lower()

        # ---------- Title ----------
        title_frame = ctk.CTkFrame(
            self.root,
            height=100,
            fg_color="#c0392b",
            corner_radius=0
        )
        title_frame.place(x=0, y=0, relwidth=1)
        title_frame.pack_propagate(False)

        ctk.CTkLabel(
            title_frame,
            text="JUST E-pay  |  Products",
            font=ctk.CTkFont(
                family="Comic Sans MS",
                size=40,
                weight="bold",
                slant="italic"
            ),
            text_color="white"
        ).place(relx=0.5, rely=0.5, anchor="center")

        # ---------- Main Container ----------
        main_frame = ctk.CTkFrame(
            self.root,
            width=1000,
            height=560,
            fg_color="white",
            corner_radius=25,
            border_width=4,
            border_color="#c0392b"
        )
        main_frame.place(relx=0.5, rely=0.57, anchor="center")
        main_frame.pack_propagate(False)

        # ---------- Scrollable Area ----------
        self.products_area = ctk.CTkScrollableFrame(
            main_frame,
            width=960,
            height=520,
            fg_color="white"
        )
        self.products_area.pack(pady=15)

        if not self.products_list:
            self.show_empty_message()
        else:
            self.render_products()

    def render_products(self):
        columns = 3

        for index, product in enumerate(self.products_list):
            row = index // columns
            column = index % columns

            card = self.create_product_card(self.products_area, product)
            card.grid(row=row, column=column, padx=20, pady=20)

    def show_empty_message(self):
        ctk.CTkLabel(
            self.products_area,
            text="No products available in this category",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#7f8c8d"
        ).pack(pady=200)

    def create_product_card(self, parent, product):
        card = ctk.CTkFrame(
            parent,
            width=280,
            height=360,
            fg_color="white",
            corner_radius=20,
            border_width=2,
            border_color="#c0392b"
        )
        card.pack_propagate(False)

        # ---------- Image Placeholder ----------
        image_placeholder = ctk.CTkFrame(
            card,
            width=220,
            height=150,
            fg_color="#ecf0f1",
            corner_radius=12
        )
        image_placeholder.pack(pady=(15, 10))

        ctk.CTkLabel(
            image_placeholder,
            text="Product Image",
            text_color="#7f8c8d"
        ).place(relx=0.5, rely=0.5, anchor="center")

        # ---------- Name ----------
        ctk.CTkLabel(
            card,
            text=product["name"],
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#2c3e50",
            wraplength=240,
            justify="center"
        ).pack(pady=(5, 5))

        # ---------- Description ----------
        ctk.CTkLabel(
            card,
            text=product["description"],
            font=ctk.CTkFont(size=13),
            text_color="#7f8c8d",
            wraplength=240,
            justify="center"
        ).pack(pady=(0, 8))

        # ---------- Price ----------
        ctk.CTkLabel(
            card,
            text=f"{product['price']} EGP",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#c0392b"
        ).pack(pady=(0, 10))

        # ---------- Add to Cart ----------
        ctk.CTkButton(
            card,
            text="ADD TO CART",
            width=200,
            height=40,
            corner_radius=20,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            font=ctk.CTkFont(weight="bold"),
            command=lambda p=product: print("Added:", p["name"])
        ).pack(pady=(5, 15))

        return card

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = ProductsUI()
    app.run()
