import unittest
from task import Task


class TestTask(unittest.TestCase):

    def test_valid_task(self):
        task = Task(1, "Learn Python", "2026-11-12", "Study")

        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Learn Python")
        self.assertEqual(task.deadline, "2026-11-12")
        self.assertEqual(task.category, "Study")
        self.assertEqual(task.priority, "Medium")
        self.assertEqual(task.status, "To Do")

    def test_title_stripping(self):
        task = Task(1, "  Learn Python  ", "2026-11-12", "Study")
        self.assertEqual(task.title, "Learn Python")

    def test_category_stripping(self):
        task = Task(1, "Learn Python", "2026-11-12", "  Study  ")
        self.assertEqual(task.category, "Study")

    def test_invalid_id(self):
        with self.assertRaises(ValueError):
            Task(-1, "Learn Python", "2026-11-12", "Study")

    def test_invalid_title(self):
        with self.assertRaises(ValueError):
            Task(1, "   ", "2026-11-12", "Study")

    def test_invalid_deadline(self):
        with self.assertRaises(ValueError):
            Task(1, "Learn Python", "2026-15-40", "Study")

    def test_invalid_deadline_type(self):
        with self.assertRaises(ValueError):
            Task(1, "Learn Python", 20261112, "Study")

    def test_invalid_category(self):
        with self.assertRaises(ValueError):
            Task(1, "Learn Python", "2026-11-12", "   ")

    def test_invalid_category_type(self):
        with self.assertRaises(ValueError):
            Task(1, "Learn Python", "2026-11-12", 123)

    def test_invalid_priority(self):
        with self.assertRaises(ValueError):
            Task(1, "Learn Python", "2026-11-12", "Study", "Urgent")

    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            Task(1, "Learn Python", "2026-11-12", "Study",
                 "Medium", "Started")


if __name__ == "__main__":
    unittest.main()
