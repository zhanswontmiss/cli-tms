from datetime import datetime

class Task:

    valid_priorities = ["Low", "Medium", "High", "Critical"]
    valid_statuses = ["To Do", "In Progress", "Completed"]

    def __init__(self, id, title, deadline, category, priority="Medium", status="To Do"):
        if type(id) is not int or id <= 0:
            raise ValueError("Invalid task ID is set!")
        
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Invalid task title is set!")

        if not isinstance(deadline, str):
            raise ValueError("Deadline must be a string!")

        try:
            datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid task deadline is set!") from None

        if not isinstance(category, str) or not category.strip():
            raise ValueError("Invalid task category is set!")
        
        if priority not in self.valid_priorities:
            raise ValueError("Invalid task priority is set!")

        if status not in self.valid_statuses:
            raise ValueError("Invalid task status is set!")

        title = title.strip()
        category = category.strip()

        self.id = id
        self.title = title
        self.deadline = deadline
        self.category = category
        self.priority = priority
        self.status = status


    def mark_as_completed(self) -> None:
        self.status = "Completed"

    def change_priority(self, priority: str) -> None:
        priorities = ["Low", "Medium", "High", "Critical"]
        if priority in priorities:
            self.priority = priority
        else:
            print("Invalid priority type")

    def update_status(self, status: str) -> None:
        statuses = ["To Do", "In Progress", "Completed"]
        if status in statuses:
             self.status = status
        else:
            print("Invalid status")
        
    def change_deadline(self, deadline) -> None:
        self.deadline = deadline

    def __str__(self) -> str:
        return (
            f"ID: {self.id} | "
            f"Title: {self.title} |"
            f"Deadline: {self.deadline} | "
            f"Category: {self.category} | "
            f"Status: {self.status} | "
            f"Priority: {self.priority} | "
        )

    def __repr__(self):
        return f"Task(title='{self.title}', status='{self.status}', priority='{self.priority}', deadline='{self.deadline}', category='{self.category}')"

    def to_dict(self):
        return { 
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "priority": self.priority,
            "deadline": self.deadline,
            "category": self.category
        }

    @classmethod
    def from_dict(cls, dct):
        return cls(
            dct["id"], 
            dct["title"], 
            dct["deadline"], 
            dct["category"],
            dct["priority"],
            dct["status"]
        )