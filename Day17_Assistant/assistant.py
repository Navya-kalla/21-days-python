from datetime import datetime
import random
import webbrowser
import day15_tic_tac_toe

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

NOTES_FILE = os.path.join(BASE_DIR, "notes.txt")
LOGS_FILE = os.path.join(BASE_DIR, "logs.txt")


# ----------------------Functions ---------------------- #

def log_activity(activity):
    with open(LOGS_FILE, "a") as file:
        now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        file.write(f"[{now}] {activity}\n")


def tell_time():
    now = datetime.now()
    print("Current Time:", now.strftime("%H:%M:%S"))


def tell_date():
    now = datetime.now()
    print("Today's Date:", now.strftime("%B %d, %Y"))


# ---------------------- Calculator ---------------------- #

def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operator (+,-,*,/,//,%): ")

        if op == "+":
            print("Answer:", num1 + num2)

        elif op == "-":
            print("Answer:", num1 - num2)

        elif op == "*":
            print("Answer:", num1 * num2)

        elif op == "/":
            print("Answer:", num1 / num2)

        elif op == "//":
            print("Answer:", num1 // num2)

        elif op == "%":
            print("Answer:", num1 % num2)

        else:
            print("Invalid Operator!")

        log_activity("Used Calculator")

    except ZeroDivisionError:
        print("Cannot divide by zero!")

    except ValueError:
        print("Please enter valid numbers!")


# ---------------------- Jokes ---------------------- #

def tell_jokes():

    jokes = [
        "Why don't scientists trust atoms? Because they make up everything! 😂",
        "Why couldn't the bicycle stand up? It was two-tired! 🚲",
        "Why don't skeletons fight? They don't have the guts! 💀",
        "Why did the computer go to therapy? Too many issues! 💻",
        "Life is short. Smile while you still have teeth! 😁",
        "Why did the tomato blush? It saw the salad dressing! 🍅",
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "What has ears but cannot hear? A cornfield! 🌽",
        "Why did the pencil get an award? It had a sharp mind! ✏️",
        "Why did the chicken join a band? Because it had drumsticks! 🥁"
    ]

    while True:
        print("\n😂", random.choice(jokes))

        ch = input("\nAnother joke? (y/n): ").lower()

        if ch == "n":
            break

    log_activity("Listened to Jokes")


# ---------------------- Websites ---------------------- #

def open_website():

    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "gmail": "https://mail.google.com",
        "github": "https://github.com",
        "chatgpt": "https://chat.openai.com"
    }

    print("\nAvailable Websites")

    for site in websites:
        print("-", site.title())

    choice = input("\nEnter website: ").lower()

    if choice in websites:
        webbrowser.open(websites[choice])
        log_activity(f"Opened {choice.title()}")

    else:
        print("Website not found!")


# ---------------------- Tic Tac Toe ---------------------- #

def tic_tac_toe():
    log_activity("Played Tic Tac Toe")
    day15_tic_tac_toe.play_game()


# ---------------------- Notes ---------------------- #

def take_notes():

    note = input("Enter note: ")

    with open(NOTES_FILE, "a") as file:
        file.write(note + "\n")

    log_activity("Added a Note")

    print("Note Saved!")


def view_notes():

    try:
        with open(NOTES_FILE, "r") as file:
            print("\n------ NOTES ------")
            print(file.read())

    except FileNotFoundError:
        print("No Notes Found!")

    log_activity("Viewed Notes")


def search_notes():

    keyword = input("Enter keyword: ").lower()

    try:
        found = False

        with open(NOTES_FILE, "r") as file:

            for line in file:

                if keyword in line.lower():
                    print(line.strip())
                    found = True

        if not found:
            print("No matching note found!")

    except FileNotFoundError:
        print("No Notes Found!")

    log_activity(f"Searched Notes ({keyword})")


def delete_notes():

    open(NOTES_FILE, "w").close()

    print("All Notes Deleted!")

    log_activity("Deleted Notes")


# ---------------------- Logs ---------------------- #

def view_logs():

    try:

        with open(LOGS_FILE, "r") as file:
            print("\n------ LOGS ------")
            print(file.read())

    except FileNotFoundError:
        print("No Logs Available!")


# ---------------------- Welcome ---------------------- #

def welcome():

    print("=" * 55)
    print("🤖PERSONAL ASSISTANT 🤖".center(55))
    tell_date()
    tell_time()
    print("=" * 55)


def display_menu():

    print("""
1. 🧮 Calculator
2. 😂 Tell Joke
3. 🌐 Open Website
4. 🎮 Tic Tac Toe
5. 📝 Take Notes
6. 📖 View Notes
7. 🔍 Search Notes
8. 🗑 Delete Notes
9. 📜 View Logs
10. 🚪 Exit
""")


# ---------------------- Main ---------------------- #

welcome()

commands = {
    "1": calculator,
    "calculator": calculator,

    "2": tell_jokes,
    "joke": tell_jokes,

    "3": open_website,
    "website": open_website,

    "4": tic_tac_toe,
    "tic": tic_tac_toe,
    "tictactoe": tic_tac_toe,

    "5": take_notes,
    "note": take_notes,

    "6": view_notes,
    "view": view_notes,

    "7": search_notes,
    "search": search_notes,

    "8": delete_notes,
    "delete": delete_notes,

    "9": view_logs,
    "logs": view_logs,
}

while True:

    display_menu()

    command = input("🤖 Enter command or number: ").lower().strip()

    if command in ["10", "exit", "quit"]:
        print("\n🤖Thank youu!")
        log_activity("Exited Assistant")
        break

    elif command in commands:

        try:
            commands[command]()

        except Exception as e:
            print("Something went wrong!")
            print(e)

    else:
        print("Invalid command! Try again.")