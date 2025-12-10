# Day 17 - Inheritance & Polymorphism

# ------------------------------
# 1. Employee and Manager (Inheritance)
# ------------------------------
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}")

    def calculate_bonus(self):
        # Base employees get 10% bonus
        return self.salary * 0.1


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)  # Inherit attributes from Employee
        self.department = department

    # Method overriding
    def calculate_bonus(self):
        # Managers get 20% bonus
        return self.salary * 0.2

    # Additional method
    def display_info(self):
        print(f"Manager ID: {self.emp_id}, Name: {self.name}, Department: {self.department}, Salary: {self.salary}")


# ------------------------------
# 2. Book and ReferenceBook (Inheritance)
# ------------------------------
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Book: {self.title}, Author: {self.author}, Price: {self.price}")

    def discount(self):
        # Standard book discount 5%
        return self.price * 0.05


class ReferenceBook(Book):
    def __init__(self, title, author, price, subject):
        super().__init__(title, author, price)
        self.subject = subject

    # Method overriding
    def discount(self):
        # Reference books have no discount
        return 0

    def display_info(self):
        print(f"Reference Book: {self.title}, Subject: {self.subject}, Author: {self.author}, Price: {self.price}")


# ------------------------------
# Example Usage (Polymorphism)
# ------------------------------

# Employee and Manager
emp1 = Employee(101, "John", 50000)
mgr1 = Manager(201, "Alice", 80000, "IT")

employees = [emp1, mgr1]  # Polymorphism: same method call, different behavior

print("------ Employee/Manager Info ------")
for emp in employees:
    emp.display_info()
    print(f"Bonus: {emp.calculate_bonus()}\n")

# Book and ReferenceBook
book1 = Book("Python Programming", "xyz", 450)
ref_book1 = ReferenceBook("Advanced Python", "xyz", 600, "Programming")

books = [book1, ref_book1]  # Polymorphism in action

print("------ Book/ReferenceBook Info ------")
for b in books:
    b.display_info()
    print(f"Discount: {b.discount()}\n")
