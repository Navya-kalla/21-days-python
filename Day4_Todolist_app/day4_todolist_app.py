task = []

while True:
    print("\n====TO DO LIST📝====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = int(input("👉Enter choice(1/2/3/4): "))
    
    if choice == 1:
        new_task = input("Enter a task (separate by ,): ").split(",")
        for item in new_task:
            task.append(item.strip())
        print(f"Current tasks: {task}")
        
    elif choice == 2:
        if len(task) == 0:
            print("No tasks to showcase")
        else:
            print("\nYour Tasks:")
            for i, j in enumerate(task, start=1):
                print(f"{i}. {j}")
                
    elif choice == 3:
        if len(task) == 0:
            print("No tasks to delete")
        else:
            del_task = int(input("❓Which task number do you want to delete: "))
            
            if del_task < 1 or del_task > len(task):
                print("Task number is not present in the todo list")
            else:
                removed = task.pop(del_task - 1)
                print(f"'{removed}' is deleted!✔️")
                
    elif choice == 4:
        print("Goodbye!👋")
        break
    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")
