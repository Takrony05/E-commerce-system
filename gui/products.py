import customtkinter as ctk
from PIL import Image
from pathlib import Path

ctk.set_appearance_mode("light")


class ProductsUI:
    def __init__(self, products_list):
        """
        products_list:
        - List جاية من الداتا بيس (دلوقتي Dummy)
        - عدد العناصر فيها هو اللي بيحدد عدد الصناديق
        """
        self.products_list = products_list

        self.root = ctk.CTk()
        self.root.title("E-JUST Store - Products")
        self.root.geometry("1100x700")
        self.root.resizable(False, False)
        self.root.configure(fg_color="#f5f5f5")

        self.setup_ui()

    def setup_ui(self):
        # الخلفيه
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

        # العنوان
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

        # الرئيسيه 
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

        # اسكرول 
        self.products_area = ctk.CTkScrollableFrame(
            main_frame,
            width=960,
            height=520,
            fg_color="white"
        )
        self.products_area.pack(pady=15)

        # عدد الصناديق = عدد المنتجات اللي داخلة
        if not self.products_list:
            # في حالة مفيش منتجات
            self.show_empty_message()
        else:
            self.render_products()

    def render_products(self):
        columns = 3 

        for index, product in enumerate(self.products_list):
            row = index // columns
            column = index % columns

            card = self.create_product_card(self.products_area)
            card.grid(row=row, column=column, padx=20, pady=20)


        # رسالة في حالة مفيش منتجات في الكاتيجوري
    def show_empty_message(self):


        ctk.CTkLabel(
            self.products_area,
            text="No products available in this category",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#7f8c8d"
        ).pack(pady=200)

    def create_product_card(self, parent):
        """
        صندوق المنتج (UI فقط)
        كل Card مستقل بذاته
        """
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

        # -------- Product Image Placeholder --------
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

        # -------- Product Name --------
        product_name = ctk.CTkLabel(
            card,
            text=product["name"],
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#2c3e50",
            wraplength=240,
            justify="center"
        )
        product_name.pack(pady=(5, 5))

        # -------- Product Description --------
        product_description = ctk.CTkLabel(
            card,
            text=product["description"],,
            font=ctk.CTkFont(size=13),
            text_color="#7f8c8d",
            wraplength=240,
            justify="center"
        )
        product_description.pack(pady=(0, 8))

        # -------- Product Price --------
        product_price = ctk.CTkLabel(
            card,
            text=f"{product['price']} EGP",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#c0392b"
        )
        product_price.pack(pady=(0, 10))

        # زرار ال cart 
        # ملحوظه يا شباب ده الي حنربط بيه البادج الاخيره 
        
        add_to_cart_btn = ctk.CTkButton(
            card,
            text="ADD TO CART",
            width=200,
            height=40,
            corner_radius=20,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            font=ctk.CTkFont(weight="bold"),
            command=lambda: None  # هيتربط بالـ Cart Logic لاحقًا
        )
        add_to_cart_btn.pack(pady=(5, 15))

        return card

    def run(self):
        self.root.mainloop()


# ================= Dummy Run =================
# if __name__ == "__main__":
#     # الداتا دي مؤقتة
#     # Backend هيشيلها ويحط بدلها DB call
#     dummy_products = [
#         {}, {}, {}, {}, {}, {}, {} , {} , {}, {}, {}, {}
#     ]

#     app = ProductsUI(dummy_products)
#     app.run()

