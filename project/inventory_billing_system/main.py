# main.py

from products import Product, Inventory
from billing import Bill, CashBill, OnlineBill
from utils import greet
from storage import log_action, save_sale

inventory = Inventory()

print("------ Inventory & Billing System ------")
username = input("Enter your name: ")
print(greet(username))

while True:
    print("\n1. Add Product")
    print("2. View Products")
    print("3. Create Bill")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        try:
            pid = input("Product ID: ")
            name = input("Product Name: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))

            p = Product(pid, name, price, stock)
            inventory.add_product(p)
            log_action(f"Added product {name}")

        except Exception:
            print("Invalid input! Try again.")

    elif choice == "2":
        print("\n--- Product List ---")
        for pid, details in inventory.products.items():
            print(f"{pid} - {details}")

    elif choice == "3":
        customer = input("Customer Name: ")
        mode = input("Payment Mode (cash/online): ")

        bill = CashBill(customer) if mode == "cash" else OnlineBill(customer)

        while True:
            pid = input("Enter product ID (or 'done'): ")
            if pid == "done":
                break

            product = inventory.get_product(pid)
            if product:
                try:
                    qty = int(input("Quantity: "))
                    if qty > product["stock"]:
                        print("Not enough stock!")
                        continue

                    bill.add_item(product, qty)
                    product["stock"] -= qty
                    save_sale(product["name"], qty, product["price"] * qty)
                    log_action(f"Sold {qty} of {product['name']}")

                except Exception:
                    print("Error: invalid quantity")
            else:
                print("Invalid product ID")

        bill.generate_invoice()
        bill.payment_method()
        inventory.save_products()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
