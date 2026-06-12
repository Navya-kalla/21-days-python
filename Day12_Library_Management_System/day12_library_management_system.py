import json

library = {}
FILE_PATH = "Library_Data.json"

def save_data():
    with open(FILE_PATH,'w') as file:
        json.dump(library,file,indent=4)

def load_data():
    global library
    try:
        with open(FILE_PATH,'r') as file:
            library = json.load(file)
            if not isinstance(library,dict):
                library = {}
    except (FileNotFoundError, json.JSONDecodeError):
        library = {}

def add_book():
    count = int(input("How many do yo want to add? "))
    for i in range(count):
        book_name = input("Enter book name: ").title()
        author_name = input("Enter author name: ").title()
        available = "Available"
        library[book_name] = {"Author" : author_name,"Availability":available}  
    save_data()
    print("Books added successfully!!")

def view_books():
    if not library:
        print("No books are found!!")
        return
    for name,details in sorted(library.items()):
        print(f"Book: {name}")
        for key,value in details.items():
            print(f"  -{key}: {value}")
        print("")

def search_book():
    book_name = input("Enter book/author name: ").lower()
    found = False
    for name,details in library.items():
        author = details.get('Author', '').lower()
        if book_name in name.lower() or book_name in author:
            print(f"Book Found!")
            print(f"--Name :{name}\n Author : {details['Author']}\n Availability:{details['Availability']}")
            found = True
    if not found:
        print("No record found!")

def borrow_book():
    book_name = input("Enter book name you want to borrow: ").title()
    if book_name in library:
        if library[book_name]["Availability"] == "Available":
            library[book_name]["Availability"] = "Borrowed"
            save_data()
            print(f"\nSuccessfully {book_name} is borrowed")
        else:
            print("\nSorry book is not available to borrow!")
    else:
        print("\nNo record found!!⚠️")

def return_book():
    book_name = input("Enter book name you want to return: ").title()
    if book_name in library:
        if library[book_name]["Availability"] == "Borrowed":
            library[book_name]["Availability"] = "Available"
            save_data()
            print(f"\nSuccessfully {book_name} is returned")
        else:
             print(f"\n'{book_name}' was not marked as borrowed.")
    else:
        print("\nNo record found!⚠️")

def count_books():
    total_books = len(library)
    borrowed_books = sum(1 for details in library.values() if details.get("Availability") == "Borrowed")
    available_books = total_books - borrowed_books
    
    print(f"Total books: {total_books}")
    print(f"Borrowed books: {borrowed_books}")
    print(f"Available books: {available_books}")

def delete_book():
    book_name = input("Enter the book name you want to delete: ").title()
    if book_name not in library:
        print("Book not found.⚠️")
        return

    library.pop(book_name)
    save_data()
    print(f"\n{book_name} deleted successfully.")


load_data()

while True:
    print("""\n📚====LIBRARY MANAGEMENT=====📚
1. Add Book
2. View Books
3. Search Book
4. Borrow Book
5. Return Book
6. Delete Book
7. Count Books
8. Exit""")
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue
    if choice == 1:
        add_book()
    elif choice == 2:
        view_books()
    elif choice == 3:
        search_book()
    elif choice == 4:
        borrow_book()
    elif choice == 5:
        return_book()
    elif choice == 6:
        delete_book()
    elif choice == 7:
        count_books()
    elif choice == 8:
        print("👋")
        break
    else:
        print("Invalid choice please select from the above options!")

