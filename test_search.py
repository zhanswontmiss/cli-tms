import unittest

from task import Task
from search import search_task


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.tasks = [
            Task(1, "Learn Python", "2026-11-15", "Study"),
            Task(2, "Build Task Manager", "2026-11-16", "Programming"),
            Task(3, "Read Python documentation", "2026-11-17", "Study")
        ]

    def test_search_by_full_title(self):
        result = search_task(self.tasks, "Learn Python")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 1)

    def test_search_by_partial_title(self):
        result = search_task(self.tasks, "Python")

        self.assertEqual(len(result), 2)

    def test_search_case_insensitive(self):
        result = search_task(self.tasks, "python")

        self.assertEqual(len(result), 2)

    def test_search_no_matches(self):
        result = search_task(self.tasks, "Java")

        self.assertEqual(result, [])

    def test_search_empty_list(self):
        result = search_task([], "Python")

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()