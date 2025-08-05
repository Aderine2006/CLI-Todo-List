#This is a simple To-Do List application in Python.
#Here i setted a file name for the todo list.
FILENAME = "Aderine's_Todo_List.txt"

#This function Loads the tasks from the file when the app starts.
def load_tasks():
    try:
        #the r mentioned in the below denotes the read mode
        with open(FILENAME, "r") as file:
            #readlines reads all the lines into the list
            #strip removes newlines \n and spaces from the start and end of each line
            
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError: #if the file is not found, we create an empty list
        print(f"{FILENAME} not found. Starting with an empty task list.")
        tasks = []
    return tasks
#This function saves the tasks to the file whenever a task is added or removed.
#It opens the file in write mode and writes each task on a new line.
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


#This function is used to add a new task to the list.
#It prompts the user for a task, checks if it's not empty and appends it
def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added!")
    else:
        print("Empty task not added.")

#This function is used to remove a task from the list.
#It displays the current tasks, prompts the user for a task number and removes the task
def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        # Get the index of the task to remove
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

#This function displays the current tasks in the list.
def view_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
    else:
        print("\nYour Tasks:")
        # Enumerate through the tasks to display them with numbers
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
        print()

# This is the main function that runs the To-Do List application.
def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# This ensures that the main function runs only when this script is executed directly.
if __name__ == "__main__":
    main()

# This is the end of the To-Do List application code.
# You can run this script to manage your tasks easily.
# I hope you find this application useful! Thank you.