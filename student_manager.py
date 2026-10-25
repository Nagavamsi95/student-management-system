import json
import os

DATA_FILE = "students.json"


def load_students():
    """Read students from the JSON file. Return an empty dict if the file is missing."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_students(students):
    """Write the students dictionary to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=4)


def add_student(students):
    student_id = input("Student ID: ").strip()
    if student_id in students:
        print("A student with this ID already exists.")
        return

    name = input("Name: ").strip()
    course = input("Course: ").strip()

    students[student_id] = {"name": name, "course": course}
    save_students(students)
    print(f"Student '{name}' added.")


def view_students(students):
    if not students:
        print("No students found.")
        return

    print(f"\n{'ID':<10}{'Name':<20}{'Course'}")
    print("-" * 45)
    for student_id, info in students.items():
        print(f"{student_id:<10}{info['name']:<20}{info['course']}")


def find_student(students):
    student_id = input("Student ID to find: ").strip()
    info = students.get(student_id)
    if info is None:
        print("Student not found.")
        return

    print(f"ID:     {student_id}")
    print(f"Name:   {info['name']}")
    print(f"Course: {info['course']}")

def update_student(students):
    student_id = input("Student ID to update: ").strip()
    if student_id not in students:
        print("Student not found.")
        return

    info = students[student_id]
    print("Press Enter to keep the current value.")

    name = input(f"Name [{info['name']}]: ").strip()
    course = input(f"Course [{info['course']}]: ").strip()

    if name:
        info["name"] = name
    if course:
        info["course"] = course

    save_students(students)
    print("Student updated.")

def show_menu():
    print("\n===== Student Management System =====")
    print("1. Add student")
    print("2. View all students")
    print("3. Find student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Add / update grade")
    print("7. Show average report")
    print("0. Exit")


def delete_student(students):
    student_id = input("Student ID to delete: ").strip()
    if student_id not in students:
        print("Student not found.")
        return

    confirm = input(f"Delete '{students[student_id]['name']}'? (y/n): ").strip().lower()
    if confirm == "y":
        del students[student_id]
        save_students(students)
        print("Student deleted.")
    else:
        print("Delete cancelled.")

def add_grade(students):
    student_id = input("Student ID: ").strip()
    if student_id not in students:
        print("Student not found.")
        return

    subject = input("Subject: ").strip()
    try:
        grade = float(input("Grade (0-100): ").strip())
    except ValueError:
        print("Please enter a number.")
        return
    if not 0 <= grade <= 100:
        print("Grade must be between 0 and 100.")
        return

    students[student_id].setdefault("grades", {})[subject] = grade
    save_students(students)
    print(f"Saved {subject}: {grade}")


def show_report(students):
    if not students:
        print("No students found.")
        return

    print(f"\n{'ID':<10}{'Name':<20}{'Average'}")
    print("-" * 45)
    for student_id, info in students.items():
        grades = info.get("grades", {})
        if grades:
            average = sum(grades.values()) / len(grades)
            avg_text = f"{average:.2f}"
        else:
            avg_text = "N/A"
        print(f"{student_id:<10}{info['name']:<20}{avg_text}")



def main():
    students = load_students()
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            find_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            add_grade(students)
        elif choice == "7":
            show_report(students)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()