import sqlite3
import csv

conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students(
        id INTEGER  PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        department TEXT,
        cgpa REAL
)""")
conn.commit()

def export_to_csv():
    cursor.execute("SELECT * FROM Students")
    records = cursor.fetchall()
    if not records:
        print("No data to export!")
        return
    with open("students.csv",'w',newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['ID','NAME','AGE','DEPARTMENT','CGPA'])
        for student in records:
            writer.writerow(student)
    print("Data exported successfully to students.csv")


def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    department = input("Enter department: ")
    cgpa = float(input("Enter CGPA: "))
    cursor.execute(
    """
    INSERT INTO Students(name,age,department,cgpa)
    VALUES(?,?,?,?)
    """,
    (name,age,department,cgpa)
    )
    conn.commit()
    print("Student successfully added!")

def view_students():
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()
    if not students:
        print("No students found!")
        return
    print("-"*40)
    for student in students:
        print(f"Id: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Age: {student[2]}")
        print(f"Department: {student[3]}")
        print(f"CGPA: {student[4]}")
        print("-"*40)


def search_student():
    search_stu_name = input("Enter student name: ")
    cursor.execute("SELECT * FROM Students WHERE LOWER(name)=LOWER(?)",(search_stu_name,))
    student = cursor.fetchone()
    if student:
        print(f"Id: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Age: {student[2]}")
        print(f"Department: {student[3]}")
        print(f"CGPA: {student[4]}")
    else:
        print("Record not found!")


def update_student():
    student_id = int(input("Enter student id: "))
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    department = input("Enter department: ")
    cgpa = float(input("Enter CGPA: "))
    cursor.execute(
                   """
                   UPDATE Students
                   SET name=?,age=?,department=?,cgpa=?
                   WHERE id=? """,
                   (name,age,department,cgpa,student_id))
    conn.commit()
    if cursor.rowcount>0:
        print("Student details updated")
    else:
        print("Not updated")


def delete_student():
    student_id = int(input("Enter student id: "))
    confirm = input(f"DO YOU REALLY WANT TO DELETE ID:{student_id} (y/n): ").lower()
    if confirm =="n":
        print("DELETION CANCELLED!")
        return
    cursor.execute("DELETE FROM Students WHERE id=?",(student_id,))
    conn.commit()
    if cursor.rowcount>0:
        print("DELETION SUCCESSFUL!")
    else:
        print("NO RECORD FOUND!")


def view_topper():
    cursor.execute("SELECT DISTINCT department FROM Students")
    departments = cursor.fetchall()
    print("---DEPARTMENT TOPPERS---")
    for dept in departments:
        cursor.execute(
            """SELECT * FROM  Students
            WHERE department =?
            ORDER BY cgpa DESC
            LIMIT 1""",(dept[0],)
        )
        topper = cursor.fetchone()
        if topper:
            print(f"Id: {topper[0]}")
            print(f"Name: {topper[1]}")
            print(f"Age: {topper[2]}")
            print(f"Department: {topper[3]}")
            print(f"CGPA: {topper[4]}")
        else:
            print("No students found!")
        print("-"*10)

def total_students():
    cursor.execute("SELECT COUNT(*) FROM Students")
    total_count = cursor.fetchone()
    print(f"Total no.of students: {total_count[0]}")


def average_cgpa():
    cursor.execute("SELECT AVG(cgpa) FROM Students")
    average = cursor.fetchone()
    print(f"Average CGPA: {average[0]:.2f}")


def min_cgpa():
    cursor.execute("SELECT MIN(cgpa) FROM Students")
    gpa = cursor.fetchone()
    if gpa is not None:
        print(f"MIN CGPA: {gpa}")
    else:
        print("NO STUDENT FOUND!")   


def display_menu():
    print("\n"+"="*40)
    print("     STUDENT MANAGEMENT SYSTEM")
    print("\n"+"="*40)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Department Toppers")
    print("7. Total Students")
    print("8. Average CGPA")
    print("9. Lowest CGPA")
    print("10. Export to CSV")
    print("11. Exit")
    print("="*50)

while True:
    display_menu()
    try:
        choice = int(input("Enter your choice: "))
        menu = {
    1: add_student,
    2: view_students,
    3: search_student,
    4: update_student,
    5: delete_student,
    6: view_topper,
    7: total_students,
    8: average_cgpa,
    9: min_cgpa,
    10: export_to_csv}
        if choice == 11:
            print("Thank you!")
            conn.close()
            break
        elif choice in menu:
            menu[choice]()
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid number!")
