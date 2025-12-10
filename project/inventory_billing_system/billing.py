# billing.py

import csv
from datetime import datetime

SALES_FILE = "data/sales.csv"


class Bill:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, product, qty):
        total = product["price"] * qty
        self.items.append({
            "name": product["name"],
            "qty": qty,
            "price": product["price"],
            "total": total
        })

    def generate_invoice(self):
        print("\n----- INVOICE -----")
        print(f"Customer: {self.customer}")
        print("-------------------")

        grand_total = 0

        for item in self.items:
            print(f"{item['name']} | Qty: {item['qty']} | Total: {item['total']}")
            grand_total += item["total"]

        gst = grand_total * 0.18
        final = grand_total + gst

        print("\nSubtotal:", grand_total)
        print("GST (18%):", gst)
        print("Final Total:", final)

        return final


class OnlineBill(Bill):
    def payment_method(self):
        print("Payment Mode: Online UPI")


class CashBill(Bill):
    def payment_method(self):
        print("Payment Mode: Cash")
