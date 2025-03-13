import os

# Function to display the menu
def display_menu():
    print("\nTo-Do List Application")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Save tasks to file")
    print("6. Load tasks from file")
    print("7. Exit")

# Function to get user choice
def get_choice():
    return input("\n\nEnter your choice: ")

def back_to_menu():
    return input("\n\nPress [Enter] to return")

# Function to add a new task
def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['task']} - {status}")

# Function to mark a task as completed
def mark_task_completed(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to mark as completed: "))
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]["completed"] = True
        print(f"Task '{tasks[task_num - 1]['task']}' marked as completed.")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: "))
    if 0 < task_num <= len(tasks):
        task = tasks.pop(task_num - 1)
        print(f"Task '{task['task']}' deleted.")
    else:
        print("Invalid task number.")

# Function to save tasks to a file
def save_tasks_to_file(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['completed']}\n")
    print("Tasks saved to file.")

# Function to load tasks from a file
def load_tasks_from_file():
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                task, completed = line.strip().split("|")
                tasks.append({"task": task, "completed": completed == "True"})
        print("Tasks loaded from file.")
    else:
        print("No saved tasks found.")
    return tasks

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



# Main function
def main():
    tasks = []
    clear_screen()
    while True:
        display_menu()
        choice = get_choice()

        match choice:
            case '1':
                add_task(tasks)
            case '2':
                clear_screen()
                view_tasks(tasks)
                back_to_menu()
            case '3':
                mark_task_completed(tasks)
            case '4':
                delete_task(tasks)
            case '5':
                save_tasks_to_file(tasks)
            case '6':
                tasks = load_tasks_from_file()
            case '7':
                print("\n\nGoodbye!\n\n")
                break
            case _:
                print("Invalid choice. Please try again.")
    

if __name__ == "__main__":
    main()