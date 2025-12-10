# storage.py

from datetime import datetime

LOG_FILE = "data/logs.txt"
SALES_FILE = "data/sales.csv"


def log_action(action):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {action}\n")


def save_sale(product_name, qty, total):
    with open(SALES_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([product_name, qty, total, datetime.now()])
