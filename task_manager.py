from task import Task
import json
import os

TASKS_FILE = "tasks.json"

class TaskManager:

    def __init__(self):
        self.tasks = { }

    def add_task(self, task: Task) -> None:
        if task.id not in self.tasks:
            self.tasks[task.id] = task
        else:
            print("Error! The task with the given ID already exists.")

    def remove_task(self, task_id: int) -> None:
        if task_id in self.tasks:
            self.tasks.pop(task_id, None)
        else:
            print("Error! The task with the given ID do not exists.")

    def get_task(self, task_id: int) -> Task | None:
        return self.tasks.get(task_id)

    def get_all_tasks(self) -> list[Task]:
        return list(self.tasks.values())

    def get_tasks_by_status(self, status: str) -> list[Task]:
        filtered_tasks = []
        for task in self.tasks.values():
            if task.status == status:
                filtered_tasks.append(task)

        return filtered_tasks

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

    def save_tasks(self):
        with open(TASKS_FILE, "w") as file:
            json.dump(
                [task.to_dict() for task in self.tasks.values()], 
                file,
                indent=4,
                ensure_ascii=False
            )

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            try:
                with open(TASKS_FILE, "r") as file:
                    loaded_tasks = json.load(file)
                
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
            except ValueError as e:
                print(f"Error: {e}")
            