import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")

def update_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    num = int(input("Enter task number to update: "))
    if 1 <= num <= len(tasks):
        new_task = input("Enter updated task: ")
        tasks[num - 1] = new_task
        save_tasks(tasks)
        print("Task updated successfully!\n")
    else:
        print("Invalid task number.\n")

def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(tasks):
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Task '{removed}' deleted successfully!\n")
    else:
        print("Invalid task number.\n")

def main():
    tasks = load_tasks()

    while True:
        print("==== TO-DO LIST MENU ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\nThanks for using the To-Do List 😊")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
