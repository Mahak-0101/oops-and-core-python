# students.py
from utils import validate_positive_int

students = []

def add_student(name, age, course):
    """Add a new student to the list."""
    age = validate_positive_int(age, "Age")
    student = {"name": name, "age": age, "course": course}
    students.append(student)
    print(f"Student added: {student}")

def display_students():
    """Display all students."""
    if not students:
        print("No students found.")
    for s in students:
        print(f"Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")
