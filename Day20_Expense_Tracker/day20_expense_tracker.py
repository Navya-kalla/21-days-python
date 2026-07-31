import sqlite3
import csv
from datetime import datetime

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    payment_mode TEXT NOT NULL,
    date TEXT NOT NULL
)
""")
conn.commit()

def add_expense():
    title=input("Enter title: ")
    amount=float(input("Enter amount: "))
    category=input("Enter category: ")
    payment=input("Enter payment mode: ")
    date=datetime.now().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO Expenses(title,amount,category,payment_mode,date) VALUES(?,?,?,?,?)",
                   (title,amount,category,payment,date))
    conn.commit()
    print("Expense added!")

def view_expenses():
    cursor.execute("SELECT * FROM Expenses")
    rows=cursor.fetchall()
    if not rows:
        print("No expenses found!")
        return
    print("-"*50)
    for r in rows:
        print(f"ID: {r[0]}")
        print(f"Title: {r[1]}")
        print(f"Amount: ₹{r[2]:.2f}")
        print(f"Category: {r[3]}")
        print(f"Payment: {r[4]}")
        print(f"Date: {r[5]}")
        print("-"*50)

def search_expense():
    title=input("Enter title: ")
    cursor.execute("SELECT * FROM Expenses WHERE title=?",(title,))
    r=cursor.fetchone()
    if r:
        print(r)
    else:
        print("Expense not found!")

def update_expense():
    eid=int(input("Enter ID: "))
    title=input("New title: ")
    amount=float(input("New amount: "))
    category=input("New category: ")
    payment=input("New payment: ")
    date=datetime.now().strftime("%Y-%m-%d")
    cursor.execute("""UPDATE Expenses
                   SET title=?,amount=?,category=?,payment_mode=?,date=?
                   WHERE id=?""",
                   (title,amount,category,payment,date,eid))
    conn.commit()
    print("Updated!" if cursor.rowcount else "ID not found!")

def delete_expense():
    eid=int(input("Enter ID: "))
    if input("Confirm (y/n): ").lower()!="y":
        return
    cursor.execute("DELETE FROM Expenses WHERE id=?",(eid,))
    conn.commit()
    print("Deleted!" if cursor.rowcount else "ID not found!")

def total_expenses():
    cursor.execute("SELECT SUM(amount) FROM Expenses")
    t=cursor.fetchone()[0] or 0
    print(f"Total Expenses: ₹{t:.2f}")

def average_expense():
    cursor.execute("SELECT AVG(amount) FROM Expenses")
    a=cursor.fetchone()[0]
    print("No expenses found!" if a is None else f"Average Expense: ₹{a:.2f}")

def lowest_expense():
    cursor.execute("SELECT * FROM Expenses ORDER BY amount ASC LIMIT 1")
    r=cursor.fetchone()
    print(r if r else "No expenses found!")

def category_statistics():
    cursor.execute("SELECT category,SUM(amount) FROM Expenses GROUP BY category")
    rows=cursor.fetchall()
    if not rows:
        print("No expenses found!")
        return
    for c,s in rows:
        print(f"{c}: ₹{s:.2f}")

def export_to_csv():
    cursor.execute("SELECT * FROM Expenses")
    rows=cursor.fetchall()
    with open("expenses.csv","w",newline="") as f:
        w=csv.writer(f)
        w.writerow(["ID","TITLE","AMOUNT","CATEGORY","PAYMENT MODE","DATE"])
        w.writerows(rows)
    print("Exported to expenses.csv")

while True:
    print("""
1.Add Expense
2.View Expenses
3.Search Expense
4.Update Expense
5.Delete Expense
6.Total Expenses
7.Average Expense
8.Lowest Expense
9.Category Statistics
10.Export to CSV
11.Exit
""")
    try:
        ch=int(input("Enter choice: "))
        if ch==1: add_expense()
        elif ch==2: view_expenses()
        elif ch==3: search_expense()
        elif ch==4: update_expense()
        elif ch==5: delete_expense()
        elif ch==6: total_expenses()
        elif ch==7: average_expense()
        elif ch==8: lowest_expense()
        elif ch==9: category_statistics()
        elif ch==10: export_to_csv()
        elif ch==11:
            break
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid number!")

conn.close()
