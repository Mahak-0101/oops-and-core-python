# Functions :- Day 1:- core_python and oops concept
# ------------------------------------------
# 1. Greet User Function
# ------------------------------------------
def greet_user(name, greeting="Hello"):
    """Greet the user with a default or custom message"""
    return f"{greeting}, {name}!"

print("------ Greeting Function ------")
name = input("Enter your name: ")
print(greet_user(name))  # Using default greeting
print(greet_user(name, "Welcome"))  # Using custom greeting
print("\n")


# ------------------------------------------
# 2. Calculate Sum of Two Numbers
# ------------------------------------------
def calculate_sum(a, b):
    """Return sum of two numbers"""
    return a + b

print("------ Sum Function ------")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Sum:", calculate_sum(x, y))
print("\n")


# ------------------------------------------
# 3. Factorial Function
# ------------------------------------------
def factorial(n):
    """Return factorial of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print("------ Factorial Function ------")
num = int(input("Enter number to find factorial: "))
print(f"Factorial of {num} is {factorial(num)}")
print("\n")


# ------------------------------------------
# 4. Reverse String Function
# ------------------------------------------
def reverse_string(s):
    """Return reversed string"""
    return s[::-1]

print("------ Reverse String Function ------")
string_input = input("Enter string to reverse: ")
print("Reversed String:", reverse_string(string_input))
print("\n")


# ------------------------------------------
# 5. Lambda Functions for Squares and Operations
# ------------------------------------------
print("------ Lambda Functions ------")
square = lambda x: x ** 2
multiply = lambda a, b: a * b
add = lambda a, b: a + b

n = int(input("Enter number to find square: "))
print(f"Square of {n} is {square(n)}")

a = int(input("Enter first number for multiplication: "))
b = int(input("Enter second number: "))
print(f"Multiplication: {multiply(a, b)}")
print(f"Addition: {add(a, b)}")
print("\n")


# ------------------------------------------
# 6. Default Arguments Example
# ------------------------------------------
print("------ Default Arguments in Function ------")
def welcome_message(user, msg="Welcome to our Python course!"):
    return f"{user}, {msg}"

print(welcome_message("Mahak"))
print(welcome_message("xyz", "Good morning! Have a great day."))
print("\n")


# ------------------------------------------
# 7. Applying Functions in Mini Project Style
# ------------------------------------------
print("------ Using Functions in Calculations ------")
def calculate_item_total(price, qty):
    return price * qty

def calculate_gst(amount, gst_rate=0.18):
    return amount * gst_rate

def generate_item_report(name, price, qty):
    total = calculate_item_total(price, qty)
    gst = calculate_gst(total)
    grand_total = total + gst
    return f"{name}: Price={price}, Qty={qty}, Total={total}, GST={gst}, Grand Total={grand_total}"

items = [
    {"name": "Milk", "price": 40, "qty": 2},
    {"name": "Bread", "price": 25, "qty": 1}
]

for item in items:
    print(generate_item_report(item["name"], item["price"], item["qty"]))

print("\n------ End of Functions Demo ------")

