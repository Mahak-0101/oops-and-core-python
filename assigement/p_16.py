# Day 16 - Constructors & Methods

# ------------------------------
# 1. Student Class with Constructor
# ------------------------------
class Student:
    def __init__(self, name, age, marks):
        self.name = name          # Name of student
        self.age = age            # Age of student
        self.marks = marks        # List of marks
        self.total = 0
        self.average = 0

    def calculate_total(self):
        self.total = sum(self.marks)
        return self.total

    def calculate_average(self):
        if len(self.marks) > 0:
            self.average = sum(self.marks) / len(self.marks)
        else:
            self.average = 0
        return self.average

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")
        print(f"Total: {self.total}, Average: {self.average:.2f}")


# ------------------------------
# 2. Employee Class with Constructor
# ------------------------------
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
        self.gross_salary = 0

    def calculate_gross_salary(self, hra=0.2, da=0.1):
        """
        Gross Salary = Basic + HRA + DA
        HRA = 20% of Basic, DA = 10% of Basic by default
        """
        self.gross_salary = self.basic_salary + (self.basic_salary * hra) + (self.basic_salary * da)
        return self.gross_salary

    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}, Basic Salary: {self.basic_salary}")
        print(f"Gross Salary: {self.gross_salary}")


# ------------------------------
# 3. Billing Class with Constructor
# ------------------------------
class BillingItem:
    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
        self.total = 0

    def calculate_total(self):
        self.total = self.price * self.quantity
        return self.total

    def display_bill(self):
        print(f"{self.item_name} - Price: {self.price}, Quantity: {self.quantity}, Total: {self.total}")


# ------------------------------
# Example Usage
# ------------------------------

# Student Example
student1 = Student("xyz", 18, [85, 90, 95])
student1.calculate_total()
student1.calculate_average()
student1.display_info()

print("\n")

# Employee Example
employee1 = Employee(101, "John", 50000)
employee1.calculate_gross_salary()
employee1.display_info()

print("\n")

# Billing Example
item1 = BillingItem("Notebook", 50, 5)
item1.calculate_total()
item1.display_bill()
