import customtkinter as ctk
from PIL import Image, ImageDraw
from pathlib import Path

from utlis.path_helper import get_image_path
from controllers.product_manager import ProductManager
from controllers.CartManager import CartManager
from models.product import Product

ctk.set_appearance_mode("light")


class ProductsUI:
    def __init__(self, user=None, category_id=None):
        self.user = user
        self.category_id = category_id

        pm = ProductManager()
        if category_id:
            self.products_list = pm.search_products(category_id=category_id)
        else:
            self.products_list = pm.get_all_products()

        self.product_images = []  # prevent GC

        self.root = ctk.CTk()
        self.root.title("E-JUST Store - Products")
        self.root.after(0, lambda: self.root.state("zoomed"))
        self.root.configure(fg_color="#f5f5f5")

        self.setup_ui()

    # ================= UI =================

    def setup_ui(self):
        base_path = Path(__file__).resolve().parent
        bg_path = base_path / "assets" / "background1.jpg"

        if bg_path.exists():
            bg_image = Image.open(bg_path)
            self.bg_image = ctk.CTkImage(
                bg_image,
                bg_image,
                size=(self.root.winfo_screenwidth(), self.root.winfo_screenheight())
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
            text="JUST E-Buy  |  Products",
            font=ctk.CTkFont(
                family="Comic Sans MS",
                size=40,
                weight="bold",
                slant="italic"
            ),
            text_color="white"
        ).place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkButton(
            title_frame,
            text="Back",
            width=120,
            height=40,
            corner_radius=20,
            fg_color="#34495e",
            hover_color="#2c3e50",
            font=ctk.CTkFont(weight="bold"),
            command=self.back_to_shop
        ).place(x=30, rely=0.5, anchor="w")

        ctk.CTkButton(
            title_frame,
            text="Cart",
            width=120,
            height=40,
            corner_radius=20,
            fg_color="#fe3636",
            hover_color="#830000",
            font=ctk.CTkFont(weight="bold"),
            command=self.open_cart
        ).place(relx=0.9, rely=0.5, anchor="center")

        # ---------- Main ----------
        main_frame = ctk.CTkFrame(
            self.root,
            width=1300,
            height=600,
            fg_color="white",
            corner_radius=25,
            border_width=4,
            border_color="#c0392b"
        )
        main_frame.place(relx=0.5, rely=0.58, anchor="center")
        main_frame.pack_propagate(False)

        self.products_area = ctk.CTkScrollableFrame(
            main_frame,
            width=1250,
            height=550,
            fg_color="white"
        )
        self.products_area.pack(pady=15)

        if not self.products_list:
            self.show_empty_message()
        else:
            self.render_products()

    # ================= PRODUCTS =================

    def render_products(self):
        columns = 5
        for index, product in enumerate(self.products_list):
            card = self.create_product_card(self.products_area, product)
            card.grid(
                row=index // columns,
                column=index % columns,
                padx=15,
                pady=20
            )

    def show_empty_message(self):
        ctk.CTkLabel(
            self.products_area,
            text="No products available",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#7f8c8d"
        ).pack(pady=200)

    # ================= IMAGE HELPERS =================

    def round_image(self, img, radius):
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle(
            (0, 0, img.size[0], img.size[1]),
            radius=radius,
            fill=255
        )
        img.putalpha(mask)
        return img

    def create_product_card(self, parent, product):
        card = ctk.CTkFrame(
            parent,
            width=220,
            height=310,
            fg_color="white",
            corner_radius=18,
            border_width=2,
            border_color="#c0392b"
        )
        card.pack_propagate(False)

        # ---------- Image ----------
        img_path = Path(get_image_path(product.image_path))
        if img_path.exists():
            img = Image.open(img_path).convert("RGBA")
            img = img.resize((200, 135), Image.LANCZOS)
            img = self.round_image(img, radius=18)

            img_ctk = ctk.CTkImage(img, img, size=(200, 135))
            self.product_images.append(img_ctk)

            ctk.CTkLabel(card, image=img_ctk, text="").pack(
                pady=(10, 8), anchor="n"
            )
        else:
            ctk.CTkLabel(
                card,
                text="No Image",
                width=180,
                height=120,
                fg_color="#ecf0f1"
            ).pack(pady=(12, 8))

        # ---------- Name ----------
        ctk.CTkLabel(
            card,
            text=product.name,
            font=ctk.CTkFont(size=16, weight="bold"),
            wraplength=200,
            justify="center"
        ).pack(pady=(4, 2))

        # ---------- Description ----------
        ctk.CTkLabel(
            card,
            text=product.description,
            font=ctk.CTkFont(size=12),
            text_color="#7f8c8d",
            wraplength=200,
            justify="center"
        ).pack(pady=(0, 6))

        # ---------- Price ----------
        ctk.CTkLabel(
            card,
            text=f"{product.price} EGP",
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color="#c0392b"
        ).pack(pady=(0, 6))

        # ---------- Add to Cart ----------
        ctk.CTkButton(
            card,
            text="ADD TO CART",
            width=170,
            height=36,
            corner_radius=18,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            font=ctk.CTkFont(size=12, weight="bold"),
            command=lambda p=product: self.add_to_cart(p)
        ).pack(pady=(4, 10))

        return card

    # ================= CART LOGIC (UNCHANGED) =================

    def add_to_cart(self, montag: Product):
        cart_manager = CartManager()
        cart_manager.add_to_cart(self.user["user_id"], montag.product_id)
        print(f"{montag.name} added to cart")

        self.show_added_to_cart_popup(montag.name)
    

    def show_added_to_cart_popup(self, product_name):
        popup = ctk.CTkToplevel(self.root)
        popup.title("Added to Cart")
        popup.geometry("420x180")
        popup.resizable(False, False)
        popup.grab_set()  

    
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - 210
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - 90
        popup.geometry(f"+{x}+{y}")


        ctk.CTkLabel(
            popup,
            text=f" {product_name} has been added to your cart.\n\nDo you want to go to the cart?",
            font=ctk.CTkFont(size=14, weight="bold"),
            justify="center"
        ).pack(pady=25)

        button_frame = ctk.CTkFrame(popup, fg_color="transparent")
        button_frame.pack(pady=10)

    
        ctk.CTkButton(
            button_frame,
            text="Continue Shopping",
            width=160,
            command=popup.destroy
        ).grid(row=0, column=0, padx=10)

        ctk.CTkButton(
            button_frame,
            text="Go to Cart",
            width=120,
            fg_color="#27ae60",
            hover_color="#1e8449",
            command=lambda: [popup.destroy(), self.open_cart()]
        ).grid(row=0, column=1, padx=10)

        popup.after(5000, popup.destroy)




    def open_cart(self):
        from gui.cart_gui import CartUI
        self.root.destroy()
        app = CartUI(self.user)
        app.run()

    def back_to_shop(self):
        from gui.shop import ShopsUI
        self.root.destroy()
        ShopsUI(self.user).run()


    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    ProductsUI().run()
