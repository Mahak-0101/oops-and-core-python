#Day 13 - File Handling
import csv
import json

# ------------------------------------------
# 1. TXT File Handling
# ------------------------------------------
print("------ TXT File Handling ------")

# Save student data to txt
students = [
    {"name": "Alice", "age": 20, "course": "Python"},
    {"name": "Bob", "age": 22, "course": "Java"}
]

# Write data
with open("students.txt", "w") as f:
    for s in students:
        f.write(f"{s['name']}, {s['age']}, {s['course']}\n")

# Read and display
print("Reading from TXT file:")
with open("students.txt", "r") as f:
    print(f.read())

# Append new student
new_student = {"name": "Charlie", "age": 21, "course": "C++"}
with open("students.txt", "a") as f:
    f.write(f"{new_student['name']}, {new_student['age']}, {new_student['course']}\n")

print("TXT file updated with new student!\n")


# ------------------------------------------
# 2. CSV File Handling
# ------------------------------------------
print("------ CSV File Handling ------")

employees = [
    {"id": 101, "name": "John", "dept": "IT"},
    {"id": 102, "name": "Jane", "dept": "HR"}
]

# Write CSV
with open("employees.csv", "w", newline="") as csvfile:
    fieldnames = ["id", "name", "dept"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for emp in employees:
        writer.writerow(emp)

# Read CSV
print("Reading from CSV file:")
with open("employees.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

# Append new employee
new_employee = {"id": 103, "name": "Mike", "dept": "Finance"}
with open("employees.csv", "a", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow(new_employee)

print("CSV file updated with new employee!\n")


# ------------------------------------------
# 3. JSON File Handling
# ------------------------------------------
print("------ JSON File Handling ------")

projects = [
    {"title": "Billing System", "status": "Completed"},
    {"title": "ATM Simulation", "status": "In Progress"}
]

# Write JSON
with open("projects.json", "w") as jsonfile:
    json.dump(projects, jsonfile, indent=4)

# Read JSON
print("Reading from JSON file:")
with open("projects.json", "r") as jsonfile:
    data = json.load(jsonfile)
    for proj in data:
        print(proj)

# Append new project
new_project = {"title": "Student Database", "status": "Pending"}
data.append(new_project)
with open("projects.json", "w") as jsonfile:
    json.dump(data, jsonfile, indent=4)

print("JSON file updated with new project!\n")


# ------------------------------------------
# ✅ Summary of File-Based Storage
# ------------------------------------------
print("All files created and updated successfully!")
print("Check 'students.txt', 'employees.csv', and 'projects.json' in your folder.")
