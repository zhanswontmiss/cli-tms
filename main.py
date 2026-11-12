from task import Task
from task_manager import TaskManager

def display_menu():
    print("\n===== TASK MANAGER =====")
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Update task status")
    print("5. Filter tasks")
    print("6. Sort tasks by deadline")
    print("7. View task by ID")
    print("0. Exit")

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(task)

def view_all_tasks(manager):
    tasks = manager.get_all_tasks()
    display_tasks(tasks)

def add_task(manager):
    try:
        task_id = int(input("Enter task ID: "))
        title = input("Enter task title: ")
        deadline = input("Enter deadline (YYYY-MM-DD): ")
        category = input("Enter category: ")
        print("\nPriorities: Low, Medium, High, Critical")
        priority = input("Enter priority: ")

        task = Task(
            task_id,
            title,
            deadline,
            category,
            priority
        )

        manager.add_task(task)
    except ValueError as e:
        print(f"Error: {e}")

def remove_task(manager):
    try: 
        task_id = int(input("Enter task ID to remove: "))
        manager.remove_task(task_id)
    except ValueError:
        print("Error: Task ID must be an integer!")

def update_task_status(manager):
    try:
        task_id = int(input("Enter task ID: "))
        task = manager.get_task(task_id)

        if task is None:
            print("Task not found!")
        else:
            print("\nAvailable statuses:")
            print("1. To Do")
            print("2. In Progress")
            print("3. Completed")

            status_choice = input("Choose new status: ")

            statuses = {
                "1": "To Do",
                "2": "In Progress",
                "3": "Completed"
            }

            if status_choice in statuses:
                task.status = statuses[status_choice]
                print("Task status updated successfully!")
            else:
                print("Invalid status choice!")
    except ValueError:
        print("Error: Task ID must be an integer!")

def filter_tasks(manager):
    print("\nFilter by:")
    print("1. Status")
    print("2. Priority")

    filter_choice = input("Choose filter: ")

    if filter_choice == "1":
        status = input("Enter status (To Do / In Progress / Completed): ")
        if status not in Task.valid_statuses:
            print("Error: Invalid status choice!")
            return
        
        tasks = manager.get_tasks_by_status(status)

    elif filter_choice == "2":
        priority = input("Enter priority (Low / Medium / High / Critical): ")
        if priority not in Task.valid_priorities:
            print("Error: Invalid priority choice!")
            return
        
        tasks = manager.get_tasks_by_priority(priority)

    else:
        print("Invalid filter choice!")
        return

    display_tasks(tasks)

def sort_tasks_by_deadline(manager):
    tasks = manager.sort_tasks_by_deadline()
    display_tasks(tasks)

def view_task_by_id(manager):
    try:
        task_id = int(input("Enter task ID: "))
        task = manager.get_task(task_id)
        if task is None:
            print("No task found.")
            return
        
        display_tasks([task])
    except ValueError:
        print("Error: Task ID must be an integer!")

# Main program
def main():
    manager = TaskManager()
    manager.load_tasks()

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "0": # 1
            manager.save_tasks()
            print("Exiting Task Manager...")
            break
        
        elif choice == "1":
            view_all_tasks(manager)
        elif choice == "2": # 2
            add_task(manager)
        elif choice == "3": # 3
            remove_task(manager)
        elif choice == "4": # 4
            update_task_status(manager)
        elif choice == "5": # 5
            filter_tasks(manager)
        elif choice == "6": # 6
            sort_tasks_by_deadline(manager)
        elif choice == "7": # 7
            view_task_by_id(manager)
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()