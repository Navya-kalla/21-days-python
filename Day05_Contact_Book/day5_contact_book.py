contacts = {}
def add_contacts(a,b):
   contacts[a]=b
   print(f"{a} contact added")

while True:
    print("""\n===== CONTACT BOOK =====
1. Add Contact
2. Search Contact
3. Delete Contact
4. View Contacts
5. Exit""")
    choice = int(input("Select operation: "))
    if choice==1:
        name=input("Enter name: ").capitalize()
        phone_number=input("Enter number: ")
        if len(phone_number)==10 and phone_number.isdigit():
            phone = int(phone_number)
        else:
            print("Invalid Phone Number!")
            continue

        if name in contacts:
            print("Contact already exists!")
        else:
            add_contacts(name,phone)
    elif choice==2:
        name = input("Enter the name to search: ").capitalize()
        print(f"{name}:{(contacts.get(name,'Not Found'))}")
    elif choice==3:
        name=input("Enter name to delete: ").capitalize()
        if name in contacts:
            print("Contact deleted")
            del contacts[name]
        else:
            print("Contact not found!")
    elif choice==4:
        if not contacts:
            print("Contacts not available")
        else:
            for i,j in contacts.items():
                print(f"{i}:{j}")
    elif choice==5:
        print("Existing Contact Book")
        break
    else:
        print("Invalid choice choose between 1,2,3,4 or 5")
