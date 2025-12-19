import customtkinter as ctk
from PIL import Image, ImageDraw
from pathlib import Path
from utlis.path_helper import get_image_path as gip
from gui.products import ProductsUI

ctk.set_appearance_mode("light")


# ================= SHOP BOX =================
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
            command=command,
            **kwargs
        )
        self.pack_propagate(False)

        # ---------- Content ----------
        content = ctk.CTkFrame(self, fg_color="transparent")
        content.pack(fill="both", expand=True)

        # ---------- Image Frame ----------
        self.img_frame = ctk.CTkFrame(
            content,
            width=210,
            height=100,
            fg_color="#ecf0f1",
            corner_radius=14
        )
        self.img_frame.pack(pady=(15, 10))
        self.img_frame.pack_propagate(False)

        # ---------- Image ----------
        if image_path:
            img_path = Path(image_path)
            if img_path.exists():
                img = Image.open(img_path).convert("RGBA")
                img = img.resize((210, 100), Image.LANCZOS)
                img = self.round_image(img, radius=14)

                self.img_ctk = ctk.CTkImage(img, img, size=(210, 100))
                img_label = ctk.CTkLabel(
                    self.img_frame,
                    image=self.img_ctk,
                    text=""
                )
                img_label.pack(expand=True)

                self.bind_all_children(img_label)

            else:
                lbl = ctk.CTkLabel(
                    self.img_frame,
                    text="Image not found",
                    text_color="#e74c3c"
                )
                lbl.place(relx=0.5, rely=0.5, anchor="center")
                self.bind_all_children(lbl)
        else:
            lbl = ctk.CTkLabel(
                self.img_frame,
                text="Shop Image",
                text_color="#7f8c8d"
            )
            lbl.place(relx=0.5, rely=0.5, anchor="center")
            self.bind_all_children(lbl)

        # ---------- Title ----------
        self.title_label = ctk.CTkLabel(
            content,
            text=title,
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#2c3e50"
        )
        self.title_label.pack(pady=(0, 15))

        self.bind_all_children(content)
        self.bind_all_children(self.img_frame)
        self.bind_all_children(self.title_label)

    # ---------- Rounded Image ----------
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

    # ---------- Make All Clickable ----------
    def bind_all_children(self, widget):
        widget.bind("<Button-1>", lambda e: self.invoke())
        widget.bind("<Enter>", lambda e: self.configure(cursor="hand2"))


# ================= SHOPS UI =================
class ShopsUI:
    def __init__(self, user=None):
        self.user = user
        self.root = ctk.CTk()
        self.root.title("JUST E-pay | Shops")
        self.root.after(0, lambda: self.root.state("zoomed"))
        self.root.state("zoomed")
        self.root.configure(fg_color="#f5f5f5")

        self.setup_ui()

    def setup_ui(self):
        # ---------- Title Bar ----------
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
            self.bg_image = ctk.CTkImage(
                bg_image,
                bg_image,
                size=(self.root.winfo_screenwidth(), self.root.winfo_screenheight())
            )
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

        # ---------- Main ----------
        main_frame = ctk.CTkFrame(
            self.root,
            width=1000,
            height=520,
            fg_color="white",
            corner_radius=25,
            border_width=4,
            border_color="#c0392b"
        )
        main_frame.place(relx=0.5, rely=0.53, anchor="center")
        main_frame.pack_propagate(False)

        # ================= Shops Grid =================
        grid_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        grid_frame.pack(pady=40)

        ShopBox(grid_frame, "All Shops", gip("all shops.jpg"),
                command=lambda: self.open_products(None)).grid(row=0, column=0, padx=25, pady=25)

        ShopBox(grid_frame, "Gift Shop", gip("Gift Shop.jpeg"),
                command=lambda: self.open_products(2)).grid(row=0, column=1, padx=25, pady=25)

        ShopBox(grid_frame, "Cafe", gip("Flavora Cafe.jpeg"),
                command=lambda: self.open_products(3)).grid(row=0, column=2, padx=25, pady=25)

        ShopBox(grid_frame, "Flower Shop", gip("Flower shop.jpeg"),
                command=lambda: self.open_products(1)).grid(row=1, column=0, padx=25, pady=25)

        ShopBox(grid_frame, "Halls", gip("Red Hall.jpeg"),
                command=lambda: self.open_products(4)).grid(row=1, column=1, padx=25, pady=25)

        ShopBox(grid_frame, "Super Market", gip("Supermarket.jpeg"),
                command=lambda: self.open_products(5)).grid(row=1, column=2, padx=25, pady=25)

        ShopBox(grid_frame, "Library", None,
                command=lambda: self.open_products(6)).grid(row=2, column=1, padx=25, pady=25)

    def open_products(self, category_id):
        self.root.destroy()
        ProductsUI(self.user, category_id).run()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    ShopsUI().run()
