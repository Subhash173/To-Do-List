# This program is a simple to-do list application

# Define a function to display the menu options
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. Edit a task")
    print("3. Delete a task")
    print("4. Mark a task as completed")
    print("5. Save tasks to file")
    print("6. Load tasks from file")
    print("7. Exit")

# Define a function to display the tasks
def display_tasks(tasks):
    print("\nTo-Do List:")
    for i, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Incomplete"
        print(f"{i + 1}. {task['description']} - {status}")

# Start with an empty list of tasks
tasks = []

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        description = input("Enter the task description: ")
        task = {"description": description, "completed": False}
        tasks.append(task)
    elif choice == '2':
        display_tasks(tasks)
        index = int(input("Enter the task number to edit: ")) - 1
        new_description = input("Enter the new task description: ")
        tasks[index]["description"] = new_description
    elif choice == '3':
        display_tasks(tasks)
        index = int(input("Enter the task number to delete: ")) - 1
        del tasks[index]
    elif choice == '4':
        display_tasks(tasks)
        index = int(input("Enter the task number to mark as completed: ")) - 1
        tasks[index]["completed"] = True
    elif choice == '5':
        filename = input("Enter the filename to save to: ")
        with open(filename, 'w') as file:
            for task in tasks:
                status = "Completed" if task["completed"] else "Incomplete"
                file.write(f"{task['description']} - {status}\n")
        print("Tasks saved to file.")
    elif choice == '6':
        filename = input("Enter the filename to load from: ")
        try:
            with open(filename, 'r') as file:
                tasks = []
                for line in file:
                    description, status = line.strip().split(' - ')
                    task = {"description": description, "completed": status == "Completed"}
                    tasks.append(task)
            print("Tasks loaded from file.")
        except FileNotFoundError:
            print("File not found. Please try again.")
    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
