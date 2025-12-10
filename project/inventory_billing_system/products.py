# products.py

import json
import os

DATA_FOLDER = "data"
DATA_FILE = f"{DATA_FOLDER}/products.json"


# Auto-create folder + file
def ensure_storage():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({}, f)


class Product:
    def __init__(self, pid, name, price, stock):
        self.pid = pid
        self.name = name
        self.price = price
        self.stock = stock

    def display(self):
        print(f"ID: {self.pid}, Name: {self.name}, Price: {self.price}, Stock: {self.stock}")


class Inventory:
    def __init__(self):
        ensure_storage()
        self.products = self.load_products()

    def load_products(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def save_products(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.products, f, indent=4)

    def add_product(self, product):
        self.products[product.pid] = {
            "name": product.name,
            "price": product.price,
            "stock": product.stock
        }
        self.save_products()
        print("✔ Product added successfully!")

    def update_stock(self, pid, qty):
        if pid in self.products:
            self.products[pid]["stock"] += qty
            self.save_products()
        else:
            print("❌ Product ID not found!")

    def get_product(self, pid):
        return self.products.get(pid, None)
