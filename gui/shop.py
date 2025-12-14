import customtkinter as ctk
from PIL import Image
from pathlib import Path

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

        # ---------- Image Placeholder ----------
        self.img_frame = ctk.CTkFrame(
            content,
            width=200,
            height=100,
            fg_color="#ecf0f1",
            corner_radius=12
        )
        self.img_frame.pack(pady=(15, 10))

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


class ShopsUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("JUST E-pay | Shops")
        self.root.geometry("1100x700")
        self.root.resizable(False, False)
        self.root.configure(fg_color="#f5f5f5")

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

                # -------- Shop 4: All Shops --------
        self.all_shop_btn = ShopBox(
            grid_frame,
            title="All Shops",
            image_path=None,
            command=lambda: print("All Shops clicked")
        )
        self.all_shop_btn.grid(row=1, column=0, padx=25, pady=25)
        
        # -------- Shop 1: Flower Shop --------
        self.flower_shop_btn = ShopBox(
            grid_frame,
            title="Flower Shop",
            image_path=None,
            command=lambda: print("Flower Shop clicked")
        )
        self.flower_shop_btn.grid(row=0, column=0, padx=25, pady=25)

        # -------- Shop 2: Gift Shop --------
        self.gift_shop_btn = ShopBox(
            grid_frame,
            title="Gift Shop",
            image_path=None,
            command=lambda: print("Gift Shop clicked")
        )
        self.gift_shop_btn.grid(row=0, column=1, padx=25, pady=25)

        # -------- Shop 3: Cafe --------
        self.cafe_shop_btn = ShopBox(
            grid_frame,
            title="Cafe",
            image_path=None,
            command=lambda: print("Cafe clicked")
        )
        self.cafe_shop_btn.grid(row=0, column=2, padx=25, pady=25)


        # -------- Shop 5: Halls --------
        self.halls_shop_btn = ShopBox(
            grid_frame,
            title="Halls",
            image_path=None,
            command=lambda: print("Halls clicked")
        )
        self.halls_shop_btn.grid(row=1, column=1, padx=25, pady=25)

        # -------- Shop 6: Super Market --------
        self.market_shop_btn = ShopBox(
            grid_frame,
            title="Super Market",
            image_path=None,
            command=lambda: print("Super Market clicked")
        )
        self.market_shop_btn.grid(row=1, column=2, padx=25, pady=25)

        # -------- Shop 7: Library --------
        self.library_shop_btn = ShopBox(
            grid_frame,
            title="Library",
            image_path=None,
            command=lambda: print("Library clicked")
        )
        self.library_shop_btn.grid(row=2, column=1, padx=25, pady=25)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = ShopsUI()
    app.run()
