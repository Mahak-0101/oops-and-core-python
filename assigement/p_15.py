# Day 15 - OOP Introduction

# ------------------------------
# 1. Student Class
# ------------------------------
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}, Course: {self.course}")

    def update_course(self, new_course):
        self.course = new_course
        print(f"{self.name}'s course updated to {self.course}")


# ------------------------------
# 2. Employee Class
# ------------------------------
class Employee:
    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department

    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}, Department: {self.department}")

    def update_department(self, new_department):
        self.department = new_department
        print(f"{self.name}'s department updated to {self.department}")


# ------------------------------
# 3. Billing Class
# ------------------------------
class BillingItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total = 0

    def calculate_total(self):
        self.total = self.price * self.quantity
        return self.total

    def display_bill(self):
        print(f"{self.name} - Price: {self.price}, Quantity: {self.quantity}, Total: {self.total}")


# ------------------------------
# Example Usage
# ------------------------------

# Create Student Object
student1 = Student("xyz", 18, "Python")
student1.display_info()
student1.update_course("Advanced Python")
student1.display_info()

print("\n")

# Create Employee Object
employee1 = Employee(101, "John", "IT")
employee1.display_info()
employee1.update_department("HR")
employee1.display_info()

print("\n")

# Create Billing Item Object
item1 = BillingItem("Notebook", 50, 5)
item1.calculate_total()
item1.display_bill()
