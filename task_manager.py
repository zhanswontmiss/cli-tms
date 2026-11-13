from task import Task
import json
import os

TASKS_FILE = "tasks.json"

class TaskManager:

    def __init__(self):
        self.tasks = {}

    def add_task(self, task: Task) -> None:
        if task.id in self.tasks:
            raise ValueError("A task with this ID already exists!")
            
        self.tasks[task.id] = task

    def remove_task(self, task_id: int) -> None:
        if task_id not in self.tasks:
            raise ValueError("Task with this ID does not exist!")

        del self.tasks[task_id]

    def get_task(self, task_id: int) -> Task | None:
        return self.tasks.get(task_id)

    def get_all_tasks(self) -> list[Task]:
        return list(self.tasks.values())

    def get_tasks_by_status(self, status: str) -> list[Task]:
        return [
            task for task in self.tasks.values()
            if task.status == status
        ]

    def get_tasks_by_priority(self, priority: str) -> list[Task]:
        return [
            task for task in self.tasks.values()
            if task.priority == priority
        ]

    def sort_tasks_by_deadline(self) -> list[Task]:
        return sorted(
            self.tasks.values(), 
            key=lambda task: task.deadline
        )

    def save_tasks(self) -> None:
        with open(TASKS_FILE, "w", encoding="utf-8") as file:
            json.dump(
                [task.to_dict() for task in self.tasks.values()], 
                file,
                indent=4,
                ensure_ascii=False
            )

    def load_tasks(self) -> None:
        if os.path.exists(TASKS_FILE):
            try:
                with open(TASKS_FILE, "r", encoding="utf-8") as file:
                    loaded_tasks = json.load(file)
                    if not isinstance(loaded_tasks, list):
                        raise ValueError("Tasks data must be a list!")
                
                new_tasks = {}
                for task in loaded_tasks:
                    if task["id"] in new_tasks:
                        raise ValueError("Duplicate task ID!")
                    else:
                        new_tasks[task["id"]] = Task.from_dict(task)

                self.tasks = new_tasks
            except json.JSONDecodeError:
                print("Error: Invalid JSON format!")

            except KeyError:
                print("Error: Missing required field in task data!")

            except (TypeError, ValueError) as e:
                print(f"Error: {e}")

    def get_task_count(self) -> int:
        return len(self.tasks)
            