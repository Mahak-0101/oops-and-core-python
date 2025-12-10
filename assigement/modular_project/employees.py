# employees.py
from utils import validate_positive_int

employees = []

def add_employee(emp_id, name, department):
    """Add a new employee to the list."""
    emp_id = validate_positive_int(emp_id, "Employee ID")
    employee = {"id": emp_id, "name": name, "department": department}
    employees.append(employee)
    print(f"Employee added: {employee}")

def display_employees():
    """Display all employees."""
    if not employees:
        print("No employees found.")
    for emp in employees:
        print(f"ID: {emp['id']}, Name: {emp['name']}, Department: {emp['department']}")
