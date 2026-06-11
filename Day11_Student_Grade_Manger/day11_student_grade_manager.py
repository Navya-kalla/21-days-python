import json

students = {}
filepath = "Student_data.json"


def save_data():
    with open(filepath, "w") as file:
        json.dump(students, file, indent=4)


def load_data():
    global students
    try:
        with open(filepath, "r") as file:
            students = json.load(file)
            if not isinstance(students, dict):
                students = {}
    except (FileNotFoundError, json.JSONDecodeError):
        students = {}


def get_marks(subject):
    while True:
        try:
            marks = int(input(f"Enter {subject} Marks: "))
            if 0 <= marks <= 100:
                return marks
            print("Marks should be between 0 and 100.")
        except ValueError:
            print("Enter a valid integer.")


def grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    return "F"


def add_student():
    name = input("Enter Student name: ").capitalize()

    if name in students:
        print("Student already exists.")
        return

    students[name] = {
        "English": get_marks("English"),
        "Telugu": get_marks("Telugu"),
        "Maths": get_marks("Maths"),
        "Science": get_marks("Science"),
        "Social": get_marks("Social")
    }

    save_data()
    print("Student added successfully.")


def view_students():
    if not students:
        print("No students available.")
        return

    for name, subjects in students.items():
        print(f"\n{name}")
        for subject, mark in subjects.items():
            print(f"{subject}: {mark} ({grade(mark)})")


def search_student():
    name = input("Enter student name: ").capitalize()

    if name not in students:
        print("Student not found.")
        return

    print(f"\n{name}")
    for subject, mark in students[name].items():
        print(f"{subject}: {mark} ({grade(mark)})")


def cal_avg(show=True):
    if not students:
        if show:
            print("No students available.")
        return {}

    averages = {
        name: sum(subjects.values()) / len(subjects)
        for name, subjects in students.items()
    }

    if show:
        for name, avg in averages.items():
            print(f"{name}: {avg:.2f}")

    return averages


def find_topper():
    averages = cal_avg(False)

    if not averages:
        print("No topper available.")
        return

    topper = max(averages, key=averages.get)

    print("\nTopper")
    print(f"Name: {topper}")
    print(f"Average: {averages[topper]:.2f}")
    print(f"Grade: {grade(averages[topper])}")


def update_student():
    name = input("Enter student name: ").capitalize()

    if name not in students:
        print("Student not found.")
        return

    for subject in students[name]:
        students[name][subject] = get_marks(subject)

    save_data()
    print("Marks updated successfully.")


def report_card():
    name = input("Enter student name: ").capitalize()

    if name not in students:
        print("Student not found.")
        return

    print(f"\nReport Card - {name}")

    total = 0

    for subject, mark in students[name].items():
        total += mark
        print(f"{subject}: {mark} ({grade(mark)})")

    average = total / len(students[name])

    print(f"Average: {average:.2f}")
    print(f"Overall Grade: {grade(average)}")


def subject_average():
    if not students:
        print("No students available.")
        return

    subjects = ["English", "Telugu", "Maths", "Science", "Social"]

    for subject in subjects:
        avg = sum(students[s][subject] for s in students) / len(students)
        print(f"{subject}: {avg:.2f}")


def student_ranking():
    averages = cal_avg(False)

    if not averages:
        print("No rankings available.")
        return

    ranked = sorted(
        averages.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRankings")

    for i, (name, avg) in enumerate(ranked, start=1):
        print(f"{i}. {name} - {avg:.2f}")


def high_low():
    name = input("Enter student name: ").capitalize()

    if name not in students:
        print("Student not found.")
        return

    highest_subject = max(students[name], key=students[name].get)
    lowest_subject = min(students[name], key=students[name].get)

    print(
        f"Highest: {highest_subject} - "
        f"{students[name][highest_subject]}"
    )

    print(
        f"Lowest: {lowest_subject} - "
        f"{students[name][lowest_subject]}"
    )


def del_student():
    name = input("Enter student name to delete: ").capitalize()

    if name not in students:
        print("Student not found.")
        return

    students.pop(name)
    save_data()
    print("Student deleted successfully.")


load_data()

while True:
    print("""
===== STUDENT GRADE MANAGER =====

1. Add Student
2. View Students
3. Search Student
4. Calculate Average
5. Find Topper
6. Delete Student
7. Highest / Lowest Score
8. Update Student Marks
9. Student Ranking
10. Subject Average
11. Report Card
12. Exit
""")

    try:
        choice = int(input("Enter option: "))
    except ValueError:
        print("Enter a valid number.")
        continue

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        cal_avg()
    elif choice == 5:
        find_topper()
    elif choice == 6:
        del_student()
    elif choice == 7:
        high_low()
    elif choice == 8:
        update_student()
    elif choice == 9:
        student_ranking()
    elif choice == 10:
        subject_average()
    elif choice == 11:
        report_card()
    elif choice == 12:
        break
    else:
        print("Invalid option.")
