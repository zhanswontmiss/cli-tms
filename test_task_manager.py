
import unittest
import json
import os
import tempfile

from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO

from task import Task
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()
        self.task = Task(
            1, "Learn Python", "2026-11-12", "Study"
        )

    def test_add_task(self):
        self.manager.add_task(self.task)

        self.assertIn(1, self.manager.tasks)
        self.assertEqual(self.manager.tasks[1], self.task)

    def test_add_duplicate_task(self):
        self.manager.add_task(self.task)

        output = StringIO()
        duplicate = Task(1, "Learn SQL", "2026-11-15", "Study")

        with redirect_stdout(output):
            self.manager.add_task(duplicate)

        self.assertEqual(self.manager.tasks[1], self.task)
        self.assertIn("already exists", output.getvalue())

    def test_remove_task(self):
        self.manager.add_task(self.task)

        self.manager.remove_task(1)

        self.assertNotIn(1, self.manager.tasks)


    def test_remove_nonexistent_task(self):
        self.manager.remove_task(999)

        self.assertEqual(len(self.manager.tasks), 0)

    def test_get_task(self):
        self.manager.add_task(self.task)

        result = self.manager.get_task(1)

        self.assertEqual(result, self.task)


    def test_get_nonexistent_task(self):
        result = self.manager.get_task(999)

        self.assertIsNone(result)

    def test_get_all_tasks(self):
        self.manager.add_task(self.task)

        result = self.manager.get_all_tasks()

        self.assertEqual(result, [self.task])

    def test_get_tasks_by_status(self):
        task2 = Task(2, "Learn SQL", "2026-11-15", "Study")

        self.manager.add_task(self.task)
        self.manager.add_task(task2)

        task2.status = "Completed"

        result = self.manager.get_tasks_by_status("To Do")

        self.assertEqual(result, [self.task])


    def test_get_tasks_by_priority(self):
        task2 = Task(2, "Learn SQL", "2026-11-15", "Study",
                    priority="High")

        self.manager.add_task(self.task)
        self.manager.add_task(task2)

        result = self.manager.get_tasks_by_priority("High")

        self.assertEqual(result, [task2])

    def test_sort_tasks_by_deadline(self):
        task2 = Task(2, "Learn SQL", "2026-11-10", "Study")
        task3 = Task(3, "Learn Java", "2026-11-20", "Study")

        self.manager.add_task(self.task)
        self.manager.add_task(task2)
        self.manager.add_task(task3)

        result = self.manager.sort_tasks_by_deadline()

        self.assertEqual(result, [task2, self.task, task3])

    def test_save_tasks(self):
        self.manager.add_task(self.task)

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "tasks.json")

            with patch("task_manager.TASKS_FILE", file_path):
                self.manager.save_tasks()

            with open(file_path, "r") as file:
                data = json.load(file)

            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["title"], "Learn Python")

    def test_load_tasks(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "tasks.json")

            data = [self.task.to_dict()]

            with open(file_path, "w") as file:
                json.dump(data, file)

            with patch("task_manager.TASKS_FILE", file_path):
                self.manager.load_tasks()

            self.assertEqual(len(self.manager.tasks), 1)
            self.assertEqual(
                self.manager.tasks[1].title,
                "Learn Python"
            )

    def test_load_invalid_json(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "tasks.json")

            with open(file_path, "w") as file:
                file.write("{invalid json}")

            output = StringIO()

            with patch("task_manager.TASKS_FILE", file_path):
                with redirect_stdout(output):
                    self.manager.load_tasks()

            self.assertIn("Invalid JSON format", output.getvalue())

    def test_load_missing_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "nonexistent.json")

            with patch("task_manager.TASKS_FILE", file_path):
                self.manager.load_tasks()

            self.assertEqual(self.manager.tasks, {})

    def test_load_duplicate_ids(self):
        existing_task = Task(10, "Existing task", "2026-11-20", "Study")
        self.manager.add_task(existing_task)

        duplicate_data = [
            self.task.to_dict(),
            self.task.to_dict()
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "tasks.json")

            with open(file_path, "w") as file:
                json.dump(duplicate_data, file)

            output = StringIO()

            with patch("task_manager.TASKS_FILE", file_path):
                with redirect_stdout(output):
                    self.manager.load_tasks()

        self.assertIs(self.manager.tasks[10], existing_task)
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertIn("Duplicate task ID", output.getvalue())

    def test_load_missing_field(self):
        existing_task = Task(10, "Existing task", "2026-11-20", "Study")
        self.manager.add_task(existing_task)

        invalid_data = [{
            "id": 2,
            "title": "Incomplete task",
            "deadline": "2026-11-12",
            "priority": "Medium",
            "status": "To Do"
        }]

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "tasks.json")

            with open(file_path, "w") as file:
                json.dump(invalid_data, file)

            output = StringIO()

            with patch("task_manager.TASKS_FILE", file_path):
                with redirect_stdout(output):
                    self.manager.load_tasks()

        self.assertIs(self.manager.tasks[10], existing_task)
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertIn("Missing required field", output.getvalue())

    def test_load_invalid_task_data(self):
        existing_task = Task(10, "Existing task", "2026-11-20", "Study")
        self.manager.add_task(existing_task)

        invalid_data = [{
            "id": 2,
            "title": "Invalid priority",
            "deadline": "2026-11-12",
            "category": "Study",
            "priority": "Urgent",
            "status": "To Do"
        }]

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "tasks.json")

            with open(file_path, "w") as file:
                json.dump(invalid_data, file)

            output = StringIO()

            with patch("task_manager.TASKS_FILE", file_path):
                with redirect_stdout(output):
                    self.manager.load_tasks()

        self.assertIs(self.manager.tasks[10], existing_task)
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertIn("Invalid task priority", output.getvalue())


if __name__ == "__main__":
    unittest.main()