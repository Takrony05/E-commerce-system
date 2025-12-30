import customtkinter as ctk
from PIL import Image
from pathlib import Path
from utlis.path_helper import get_image_path as gip
from gui.products import ProductsUI
from models.product import Product

ctk.set_appearance_mode("light")

class ShopBox(ctk.CTkButton):
    def __init__(self, parent, title, image_path=None, command=None, **kwargs):
        super().__init__(
            parent,
            width=260,
            height=180,
            corner_radius=20,
            fg_color="#ffffff",
            hover_color="#f0f0f0",
            border_width=2,
            border_color="#c0392b",
            text="",
            command=command if command else lambda: print(f"{title} clicked"),
            **kwargs
        )
        self.pack_propagate(False)

        content = ctk.CTkFrame(self, fg_color="transparent")
        content.pack(expand=True)

        # ---------- Image Frame ----------
        self.img_frame = ctk.CTkFrame(
            content,
            width=200,
            height=100,
            fg_color="#ecf0f1",
            corner_radius=12
        )
        self.img_frame.pack(pady=(15, 10))
        self._bind_click(self.img_frame)

        # ---------- Load Image if provided ----------
        if image_path:
            img_path = Path(image_path)
            if img_path.exists():
                img = Image.open(img_path).resize((200, 100))
                self.img_ctk = ctk.CTkImage(light_image=img, dark_image=img, size=(200, 100))
                img_label = ctk.CTkLabel(self.img_frame, image=self.img_ctk, text="")
                img_label.image = self.img_ctk  # Keep reference
                img_label.pack(expand=True)
                self._bind_click(img_label)
            else:
                ctk.CTkLabel(
                    self.img_frame,
                    text="Image not found",
                    text_color="#e74c3c"
                ).place(relx=0.5, rely=0.5, anchor="center")
        else:
            ctk.CTkLabel(
                self.img_frame,
                text="Shop Image",
                text_color="#7f8c8d"
            ).place(relx=0.5, rely=0.5, anchor="center")

        # ---------- Shop Title ----------
        self.title_label = ctk.CTkLabel(
            content,
            text=title,
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#2c3e50"
        )
        self.title_label.pack(pady=(0, 15))
        self._bind_click(self.title_label)
    
    def _bind_click(self, widget):
        widget.bind("<Button-1>", lambda e: self.invoke())


class ShopsUI:
    def __init__(self, user=None):
        self.user = user
        self.root = ctk.CTk()
        self.root.title("JUST E-BUY | Shops")
        self.root.after(0, lambda: self.root.state("zoomed"))
        self.root.state("zoomed")
        self.root.configure(fg_color="#f5f5f5")
        self.root.iconbitmap(gip("icon.ico"))
        self.setup_ui()

    def setup_ui(self):
        # ================= Title Bar =================
        title_frame = ctk.CTkFrame(
            self.root,
            height=100,
            fg_color="#c0392b",
            corner_radius=0
        )
        title_frame.place(x=0, y=0, relwidth=1)
        title_frame.pack_propagate(False)

        base_path = Path(__file__).resolve().parent
        bg_path = base_path / "assets" / "background1.jpg"

        if bg_path.exists():
            bg_image = Image.open(bg_path)
            self.bg_image = ctk.CTkImage(bg_image, bg_image, size=(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
            bg_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            bg_label.lower()

        ctk.CTkLabel(
            title_frame,
            text="JUST E-pay  |  Shops",
            font=ctk.CTkFont(
                family="Comic Sans MS",
                size=40,
                weight="bold",
                slant="italic"
            ),
            text_color="white"
        ).place(relx=0.5, rely=0.5, anchor="center")

        # ================= Main Container =================
        main_frame = ctk.CTkFrame(
            self.root,
            width=1000,
            height=520,
            fg_color="white",
            corner_radius=25,
            border_width=4,
            border_color="#c0392b"
        )
        main_frame.place(relx=0.5, rely=0.58, anchor="center")
        main_frame.pack_propagate(False)

        # ================= Shops Grid =================
        grid_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        grid_frame.pack(pady=40)

        # -------- Shop 1: Flower Shop --------
        self.flower_shop_btn = ShopBox(
            grid_frame,
            title="Flower Shop",
            image_path=gip("Flower shop.jpeg"),
            command=lambda: self.open_products(1)
        )
        self.flower_shop_btn.grid(row=1, column=0, padx=25, pady=25)

        # -------- Shop 2: Gift Shop --------
        self.gift_shop_btn = ShopBox(
            grid_frame,
            title="Gift Shop",
            image_path=gip("Gift Shop.jpeg"),
            command=lambda: self.open_products(2)
        )
        self.gift_shop_btn.grid(row=0, column=1, padx=25, pady=25)

        # -------- Shop 3: Cafe --------
        self.cafe_shop_btn = ShopBox(
            grid_frame,
            title="Cafe",
            image_path=gip("Flavora Cafe.jpeg"),
            command=lambda: self.open_products(3)
        )
        self.cafe_shop_btn.grid(row=0, column=2, padx=25, pady=25)

        # -------- Shop 4: All Shops --------
        self.all_shop_btn = ShopBox(
            grid_frame,
            title="All Shops",
            image_path=gip("all shops.jpg"),
            command=lambda: self.open_products(None)
        )
        self.all_shop_btn.grid(row=0, column=0, padx=25, pady=25)

        # -------- Shop 5: Halls --------
        self.halls_shop_btn = ShopBox(
            grid_frame,
            title="Halls",
            image_path=gip("Red Hall.jpeg"),
            command=lambda: self.open_products(4)
        )
        self.halls_shop_btn.grid(row=1, column=1, padx=25, pady=25)

        # -------- Shop 6: Super Market --------
        self.market_shop_btn = ShopBox(
            grid_frame,
            title="Super Market",
            image_path=gip("Supermarket.jpeg"),
            command=lambda: self.open_products(5)
        )
        self.market_shop_btn.grid(row=1, column=2, padx=25, pady=25)

        # -------- Shop 7: Library --------
        self.library_shop_btn = ShopBox(
            grid_frame,
            title="Library",
            image_path=None,
            command=lambda: self.open_products(6)
        )
        self.library_shop_btn.grid(row=2, column=1, padx=25, pady=25)

    def open_products(self, category_id):
        self.root.destroy()
        app = ProductsUI(self.user, category_id)
        app.run()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = ShopsUI()
    app.run()
