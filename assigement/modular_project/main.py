# main.py
from utils import greet_user, calculate_total, calculate_gst
import students
import employees

print("------ Welcome to Modular Project ------")

# Greet User
name = input("Enter your name: ")
print(greet_user(name, "Welcome"))

while True:
    print("\n--- Menu ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Add Employee")
    print("4. Display Employees")
    print("5. Billing Example")
    print("6. Exit")
    
    try:
        choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 6.")
        continue
    
    if choice == 1:
        # Add Student
        s_name = input("Enter student name: ")
        try:
            s_age = int(input("Enter student age: "))
        except ValueError:
            print("Invalid age! Must be a number.")
            continue
        s_course = input("Enter course: ")
        students.add_student(s_name, s_age, s_course)
    
    elif choice == 2:
        # Display Students
        print("\nAll Students:")
        students.display_students()
    
    elif choice == 3:
        # Add Employee
        try:
            e_id = int(input("Enter Employee ID: "))
        except ValueError:
            print("Invalid Employee ID! Must be a number.")
            continue
        e_name = input("Enter Employee Name: ")
        e_dept = input("Enter Department: ")
        employees.add_employee(e_id, e_name, e_dept)
    
    elif choice == 4:
        # Display Employees
        print("\nAll Employees:")
        employees.display_employees()
    
    elif choice == 5:
        # Billing Example
        print("\n------ Billing Example ------")
        try:
            price = float(input("Enter item price: "))
            qty = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid input! Price must be a number and quantity must be an integer.")
            continue
        total = calculate_total(price, qty)
        gst = calculate_gst(total)
        grand_total = total + gst
        print(f"Price: {price}, Quantity: {qty}, Total: {total}, GST: {gst}, Grand Total: {grand_total}")
    
    elif choice == 6:
        print("Exiting program. Goodbye!")
        break
    
    else:
        print("Invalid choice! Enter a number between 1 and 6.")
