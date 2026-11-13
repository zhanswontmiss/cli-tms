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

    def test_update_status(self):
        task = Task(1, "Learn Python", "2026-11-12", "Study")

        task.update_status("In Progress")

        self.assertEqual(task.status, "In Progress")


    def test_update_invalid_status(self):
        task = Task(1, "Learn Python", "2026-11-12", "Study")

        with self.assertRaises(ValueError):
            task.update_status("Started")

        self.assertEqual(task.status, "To Do")


    def test_change_priority(self):
        task = Task(1, "Learn Python", "2026-11-12", "Study")

        task.change_priority("Critical")

        self.assertEqual(task.priority, "Critical")


    def test_change_invalid_priority(self):
        task = Task(1, "Learn Python", "2026-11-12", "Study")

        with self.assertRaises(ValueError):
            task.change_priority("Urgent")

        self.assertEqual(task.priority, "Medium")

    def test_change_deadline(self):
        task = Task(1, "Learn Python", "2026-11-12", "Study")

        task.change_deadline("2026-12-01")

        self.assertEqual(task.deadline, "2026-12-01")


    def test_change_deadline_invalid_format(self):
        task = Task(1, "Learn Python", "2026-11-12", "Study")

        with self.assertRaises(ValueError):
            task.change_deadline("01-12-2026")

        self.assertEqual(task.deadline, "2026-11-12")


    def test_change_deadline_invalid_type(self):
        task = Task(1, "Learn Python", "2026-11-12", "Study")

        with self.assertRaises(ValueError):
            task.change_deadline(20261201)

        self.assertEqual(task.deadline, "2026-11-12")


if __name__ == "__main__":
    unittest.main()
