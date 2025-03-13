import os

class TaskTracker:

    def __init__(self):
        self.tasks = []

    # Function to display the menu
    def display_menu(self):
        print("\nTo-Do List Application")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Save tasks to file")
        print("6. Load tasks from file")
        print("7. Exit")

    # Function to get user choice
    def get_choice(self):
        return input("\n\nEnter your choice: ")

    def back_to_menu(self):
        return input("\n\nPress [Enter] to return")
    
    # Function to add a new task
    def add_task(self):
        task = input("Enter the new task: ")
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")

    # Function to view all tasks
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for i, task in enumerate(self.tasks, 1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['task']} - {status}")

    # Function to mark a task as completed
    def mark_task_completed(self):
        self.view_tasks()
        task_num = int(input("Enter the task number to mark as completed: "))
        if 0 < task_num <= len(self.tasks):
            self.tasks[task_num - 1]["completed"] = True
            print(f"Task '{self.tasks[task_num - 1]['task']}' marked as completed.")
        else:
            print("Invalid task number.")

    # Function to delete a task
    def delete_task(self):
        self.view_tasks()
        task_num = int(input("Enter the task number to delete: "))
        if 0 < task_num <= len(self.tasks):
            task = self.tasks.pop(task_num - 1)
            print(f"Task '{task['task']}' deleted.")
        else:
            print("Invalid task number.")

    # Function to save tasks to a file
    def save_tasks_to_file(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task['task']}|{task['completed']}\n")
        print("Tasks saved to file.")

    # Function to load tasks from a file
    def load_tasks_from_file(self):
        self.tasks = []

        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                for line in file:
                    task, completed = line.strip().split("|")
                    self.tasks.append({"task": task, "completed": completed == "True"})
            print("Tasks loaded from file.")
        else:
            print("No saved tasks found.")
        return self.tasks
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')