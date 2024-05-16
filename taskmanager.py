def main():
    tasks = []
    print("Welcome to Python Task Manager")
    
    def add(task):
        print("Adding your task...")
        tasks.append(task)
        
    def delete(task):
        print("""
              
              Delete

              """)
        if task in tasks:
            tasks.remove(task)
            print("Task deleted successfully!")
        else:
            print("Task not found!")
    
    def view():
        print("""
              
              Your Tasks!!!
              
              """)
        if tasks:
            print("Your tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks added yet!")
    
    
    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. View tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            new_task = input("Enter the task to add: ")
            add(new_task)
        elif choice == "2":
            task_to_delete = input("Enter the task to delete: ")
            delete(task_to_delete)
        elif choice == "3":
            print("Your tasks:")
            view()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
