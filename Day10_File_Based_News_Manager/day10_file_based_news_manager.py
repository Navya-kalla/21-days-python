from datetime import datetime
def date():
    now = datetime.now()
    return now.strftime("%Y-%m-%d , %H:%M")

def add_notes(note):
    with open("day_10.txt",'a') as file:
        file.writelines(f"[{date()}] {note} \n")
    print("Note added successfully!!")

def view_note():
    try:
        with open("day_10.txt",'r') as file:
            notes = file.readlines()
            if not notes:
                print("No notes are available")
            print("===NOTES===")
            for i,line in enumerate(notes,start=1):
                print(f"{i}. {line.strip()}")
    except FileNotFoundError:
        print("No notes found!!")

def search_note():
    try:
        se_note = input("Enter which note you want to search: ").capitalize()
        with open("day_10.txt",'r') as file:
            notes = file.readlines()
            found = False
            for line in notes:
                if se_note.lower() in line.lower():
                    print(line.strip())
                    found = True
            if not found:
                print("No such note is present!!")
    except:
        print("No such note is present!")

def delete_specific_note(del_note):
    try:
        with open("day_10.txt",'r') as file:
            lines = file.readlines()
        with open("day_10.txt",'w') as file:
            for line in lines:
                if del_note not in line:
                    file.write(line)
        print("Note deleted successfully!!")
    except:
        print("No notes exist to delete!")

def del_all_notes():
    confrim = input("Are you sure you want to delete all notes? (yes/no): ").lower()
    if confrim == 'yes':
        with open("day_10.txt",'w') as file:
            file.write("")
        print("All notes deleted successfully!!")
    else:
        print("Operation cancelled!!")


while True:
    print("""\n===NOTES MANAGER===
    1.Add note
    2.View note
    3.Search note
    4.Delete note
    5.Delete all notes
    6.Exit""")
    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        note = input("Enter note : ").capitalize()
        add_notes(note)

    elif choice == 2:
        view_note()

    elif choice == 3:
        search_note()

    elif choice == 4:
        del_note = input("Enter which note you want to delete: ").capitalize()
        delete_specific_note(del_note)

    elif choice == 5:
        del_all_notes()

    elif choice == 6:
        print("Thank you!!!")
        break

    else:
        print("Invalid choice!!")