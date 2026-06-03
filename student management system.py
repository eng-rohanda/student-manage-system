import json

students = []

def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")

    student = {
        "name": name,
        "age": age
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    for student in students:
        print(student)

def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file)

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Save & Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        save_data()
        break