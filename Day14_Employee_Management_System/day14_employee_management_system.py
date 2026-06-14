import json

employees = {}
FILE_PATH = "Employees_data.json"

def save_data():
    with open(FILE_PATH,"w") as file:
        json.dump(employees,file,indent=4)

def load_data():
    global employees
    try:
        with open(FILE_PATH,"r") as file:
            employees = json.load(file)
            if not isinstance(employees,dict):
                employees = {}
    except(FileNotFoundError,json.JSONDecodeError):
        print("No such file exists")
        employees = {}

def add_employee():
    employee_num = input("Enter employee no(EMP): ")
    if employee_num not in employees:
        emp_name = input("Enter employee name: ").title()
        emp_age = int(input("Enter employee age: "))
        emp_departmet = input("Enter employee department: ")
        emp_salary = int(input("Enter employee salary: "))
        employees[employee_num] = {"name": emp_name,
        "age": emp_age,
        "department": emp_departmet,
        "salary": emp_salary}
        save_data()
        print("Added Successfully!")
    else:
        print("Employee number already exists!!")

def avg_salary():
    total_payroll = sum(info["salary"] for info in employees.values())
    print(f"Average salary: {total_payroll/len(employees)}")

def view_employees():
    if not employees:
        print("No employee data found.")
        return
    
    sorted_employees = sorted(employees.items(), key=lambda item: item[1]["salary"], reverse=True)
    
    for id, details in sorted_employees:
        print(f"\nID: {id}")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Department: {details['department']}")
        print(f"Salary: {details['salary']}")
        print('-'*10)

def search_employee():
    try:
        emp_id = input("Enter emp id: ")
        if emp_id in employees:
            print(f"Employee Id: {emp_id}")
            print(f"Name: {employees[emp_id]['name']}")
            print(f"Age: {employees[emp_id]['age']}")
            print(f"Department: {employees[emp_id]['department']}")
            print(f"Salary: {employees[emp_id]['salary']}")
        else: 
            print("NO RECORD FOUND!")
    except:
        print("ERROR!")

def update_employee():
    emp_id = input("Enter emp id: ")
    if emp_id in employees:
        employees[emp_id]['name'] = input("Enter employee name: ").title()
        employees[emp_id]['age'] = int(input("Enter employee age:"))
        employees[emp_id]['department'] = input("Enter employee department: ")
        employees[emp_id]['salary'] = int(input("Enter employee salary: "))
        save_data()
        print("UPDATION SUCCESSFUL!")
    else: 
         print("NO RECORD FOUND!")

def delete_employee():
    emp_id = input("Enter employee id: ")
    if emp_id in employees:
        del employees[emp_id]
        save_data()
        print("Deletion successful!")
    else:
        print("No record!")

def cal_annual_salary():
    emp_id = input("Enter employee id: ")
    if emp_id in employees:
        monthly_sal = employees[emp_id]['salary']
        annual_sal = monthly_sal*12
        print(f"{employees[emp_id]['name']}")
        print(f"MONTHLY SALARY: {monthly_sal}")
        print(f"ANNUAL SALARY: {annual_sal}")
       
def highest_paid_salary():
    highest_sal = max(employees.items(), key=lambda x:x[1]['salary'])
    print(f"Employee Id: {highest_sal[0]}")
    print(f"Name: {highest_sal[1]['name']}")
    print(f"Department: {highest_sal[1]['department']}")
    print(f"Salary: {highest_sal[1]['salary']}")

def count_by_department():
    dept_counts = {}
    
    for id, details in employees.items():
        dept = details["department"]
        
        if dept in dept_counts:
            dept_counts[dept] += 1
        else:
            dept_counts[dept] = 1
            
    print("--- Employee Count by Department ---")
    print(f"Employee count: {len(employees)}")
    for dept, count in dept_counts.items():
        print(f"{dept} : {count}")

def sal_rise():
    emp_id = input("Enter employee id: ")
    if emp_id in employees:
        raise_percent = int(input("How much percentage you want to raise: "))
        print(f"Current salary: {employees[emp_id]['salary']}")
        amount = (employees[emp_id]['salary']*raise_percent)/100
        employees[emp_id]['salary'] += amount
        print(f"New salary: {employees[emp_id]['salary']}")
        save_data()
    else:
        print("No record found!")
load_data()

while True:
    print("""========= EMPLOYEE MANAGEMENT =========

1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Calculate Annual Salary
7. Highest Paid Employee
8. Employee count
9. Average salary 
10. Salary Rise       
11. Exit""")
    try:
        choice = int(input("Enter the choice: "))
    except ValueError:
        print("Please enter a valid choice.")
        continue
    if choice == 1:
        add_employee()
    elif choice == 2:
        view_employees()
    elif choice == 3:
        search_employee()
    elif choice == 4:
        update_employee()
    elif choice == 5:
        delete_employee()
    elif choice == 6:
        cal_annual_salary()
    elif choice == 7:
        highest_paid_salary()
    elif choice == 8:
        count_by_department()
    elif choice == 9:
        avg_salary()
    elif choice == 10:
        sal_rise()
    elif choice == 11:
        break
    else:
        print("INVALID CHOICE")