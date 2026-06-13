import json
import time
from datetime import date

accounts = {}
FILE_PATH = "Accounts_data.json"
DAILY_LIMIT = 20000

def save_data():
    with open(FILE_PATH,"w") as file:
        json.dump(accounts,file,indent=4)

def load_data():
    global accounts
    try:
        with open(FILE_PATH, "r") as file:
            accounts = json.load(file)
            if not isinstance(accounts, dict):
                accounts = {}
    except FileNotFoundError:
        print(f"Error: The file '{FILE_PATH}' does not exist in this folder.")
        accounts = {}
    except json.JSONDecodeError as e:
        print(f"Error: Your JSON file has invalid formatting. Details: {e}")
        accounts = {}

def check_pin(user_pin):
    for accno,details in accounts.items():
            if user_pin == details['pin']:
                return accno
    return None

def check_balance(acc_num):
    print(f"Total balance: {accounts[acc_num]['balance']}")

def reciept(acc_num):
    print("\n===RECIEPT===")
    print(f"Transaction: {accounts[acc_num]['transactions'][-1]}")  
    print(f"Balance: {accounts[acc_num]['balance']}")  

def deposit_money(acc_num):
    deposited_money = int(input("Enter amount to deposit: "))
    accounts[acc_num]['balance'] += deposited_money
    accounts[acc_num]['transactions'].append(f"Deposited {deposited_money}")
    save_data()
    print("Deposit successful")

def withdraw_money(acc_num):
    print("\n==== WITHDRAW CASH ====")
    user_data = accounts[acc_num]
    today_str = str(date.today())  
    if user_data.get("last_withdrawal_date") != today_str:
        user_data["daily_withdrawn"] = 0
        user_data["last_withdrawal_date"] = today_str

    remaining_limit = DAILY_LIMIT - user_data["daily_withdrawn"]
    print(f"Your remaining daily withdrawal limit: ₹{remaining_limit}")

    try:
        amount = float(input("Enter amount to withdraw: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    if amount <= 0:
        print("Amount must be greater than zero!")
    elif amount > user_data["balance"]:
        print("Transaction Declined: Insufficient account balance!")
    elif amount > remaining_limit:
        print(f"Transaction Declined: Exceeds your remaining daily limit of ₹{remaining_limit}!")
    else:
        user_data["balance"] -= amount
        user_data["daily_withdrawn"] += amount
        user_data["transactions"].append(f"Withdrew {amount}")
        
        save_data()  
        print(f"Success! ₹{amount} withdrawn.")
        print(f"New Balance: ₹{user_data['balance']}")


def transaction_history(acc_num):
    print("\n====MINI STATEMENT====")
    history = accounts[acc_num]['transactions'][-5:]
    if not history:
        print("NO RECENT TRANSACTIONS FOUND!")
    for i,j in enumerate(history,start=1):
        print(f"{i}. {j}")

def change_pin(acc_num):
    y_n = input("Do you want to change the pin(y/n): ").lower()
    if y_n == "y":
        present_pin = int(input("Enter current PIN: "))
        new_pin = int(input("Enter new PIN: "))
        confirm_pin = int(input("Confirm new PIN: "))
        if new_pin == confirm_pin and present_pin !=new_pin:
            accounts[acc_num]['pin'] = new_pin
            save_data()
            print("Pin changed!")

load_data()

print("====WELCOME====")
print("Please insert your card!!")

time.sleep(3)
attempts = 3

while attempts >0:
    try:
        user_pin=int(input("Enter your 4-digit pin: "))
    except ValueError:
        print("Invalid enter only 4 digits!")
        continue
    matched_account = check_pin(user_pin)
    if matched_account:
        user_name = accounts[matched_account]['Name']
        while True:
            print("""   ========= ATM =========

    1. Check Balance
    2. Deposit Money
    3. Withdraw Money
    4. Transaction History
    5. Change PIN
    6. Exit""")
            try:
                choice = int(input("Enter option: "))
            except ValueError:
                print("Please enter a valid operation!!")
                continue
            if choice == 1:
                check_balance(matched_account)
            elif choice == 2:
                deposit_money(matched_account)
            elif choice == 3:
                withdraw_money(matched_account)
            elif choice == 4:
                transaction_history(matched_account)
            elif choice == 5:
                change_pin(matched_account)
            elif choice == 6:
                reciept(matched_account)
                print("Thank you!!!")
                exit()
            else:
                print("INVALID OPTION PLEASE CHOOSE BETWEEN THE ABOVE OPTIONS!")
    else:
        attempts -= 1
        print(f"Incorrect PIN. Attempts remaining: {attempts}")
if attempts == 0:
    print("ACCESS DENIED!")