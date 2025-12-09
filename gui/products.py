import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
# AI , AI , AI , AI , AI , AI , AI , AI , AI , AI , AI , AI , AI 
class ProductsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg="#f5f5f5")
        self.create_ui()
        self.load_products()

    def create_ui(self):
        # عنوان الصفحة
        title = tk.Label(self, text="Our Products", font=("Arial", 24, "bold"), bg="#f5f5f5")
        title.pack(pady=20)

        # إطار للسكورول
        container = tk.Frame(self, bg="#f5f5f5")
        container.pack(fill=tk.BOTH, expand=True)

        # Canvas + Scrollbar
        canvas = tk.Canvas(container, bg="#f5f5f5", highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg="#f5f5f5")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def load_products(self):
        # اتصال بقاعدة البيانات
        conn = sqlite3.connect("database/DataBase.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, image_path, description FROM products")
        products = cursor.fetchall()

        # عرض المنتجات
        for index, product in enumerate(products):
            pid, name, img_path, desc = product

            # إطار لكل منتج
            frame = tk.Frame(self.scrollable_frame, bg="white", bd=2, relief="groove")
            frame.grid(row=index//3, column=index%3, padx=20, pady=20, sticky="nsew")

            # صورة المنتج
            try:
                img = Image.open(img_path)
                img = img.resize((150, 150), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(img)
                img_label = tk.Label(frame, image=photo, bg="white")
                img_label.image = photo  # مهم لحفظ المرجع
                img_label.pack(pady=10)
            except:
                img_label = tk.Label(frame, text="No Image", bg="white")
                img_label.pack(pady=10)

            # اسم المنتج
            tk.Label(frame, text=name, font=("Arial", 14, "bold"), bg="white").pack(pady=5)

            # وصف المنتج
            tk.Label(frame, text=desc, font=("Arial", 10), bg="white", wraplength=180, justify="center").pack(pady=5)

        conn.close()


# تشغيل التجربة مباشرة
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x600")
    root.title("Products Page")
    ProductsPage(root).pack(fill="both", expand=True)
    root.mainloop()