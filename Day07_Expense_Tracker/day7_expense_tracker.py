expenses=[]
print("====EXPENSE TRACKER====")
while True:
   print("""1. Add Expense
2. View Expenses
3. Show Total Spending
4. Delete Expense
5. Track Highest Expense
6. Average of expenses
7. Exit""")
   choice = int(input("Enter task(1/2/3/4): "))
   if choice==1:
        category = input("Enter category: ").capitalize()
        amount = float(input("Enter amount: "))
        expenses.append({"category":category,"amount":amount})
    
   elif choice == 2:
        for i,j in enumerate(expenses,start=1):
            print(f"{i}.{j['category']} - ₹{j['amount']}")

   elif choice == 3:
        total=0
        for i in expenses:
            total += i['amount']
        print(f"Total Expense: {total}")

   elif choice == 4:
       del_expense = int(input("Enter the expense number: "))
       del expenses[del_expense-1]
       print(f"{del_expense} deleted")

   elif choice == 5:
        if not expenses:
            print("No expenses recorded yet.")
        else:
            # FIXED: Added 'key=' before the lambda function
            highest_expense = max(expenses, key=lambda x: x['amount'])
            print(f"Highest expense : {highest_expense['category']} - ₹{highest_expense['amount']}")
   elif choice == 6:
       total=0
       for i in expenses:
            total += i['amount']
       avg = total/len(expenses)
       print(f"Average of Expenses:₹{avg:.2f}")

   elif choice == 7:
       print("Existed successfully")
       break
   
   else:
       print("INVALID CHOICE!!")