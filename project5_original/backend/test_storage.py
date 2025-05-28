import unittest
from datetime import date
from storage import TodoStorage

class TestTodoStorage(unittest.TestCase):
    def setUp(self):
        self.storage = TodoStorage()

    def test_add_and_get_todo(self):
        todo = self.storage.add_todo("Test Task 1", status=False, due_date=date(2024, 6, 30))
        self.assertEqual(todo.title, "Test Task 1")
        self.assertFalse(todo.status)
        self.assertEqual(todo.due_date, date(2024, 6, 30))
        fetched = self.storage.get_todo(todo.id)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.title, "Test Task 1")

    def test_list_todos(self):
        self.storage.add_todo("Task 1")
        self.storage.add_todo("Task 2")
        todos = self.storage.list_todos()
        self.assertEqual(len(todos), 2)
        self.assertEqual(todos[0].title, "Task 1")
        self.assertEqual(todos[1].title, "Task 2")

    def test_update_todo(self):
        todo = self.storage.add_todo("Initial", status=False)
        updated = self.storage.update_todo(todo.id, title="Updated", status=True)
        self.assertIsNotNone(updated)
        self.assertEqual(updated.title, "Updated")
        self.assertTrue(updated.status)

    def test_delete_todo(self):
        todo = self.storage.add_todo("To be deleted")
        result = self.storage.delete_todo(todo.id)
        self.assertTrue(result)
        self.assertIsNone(self.storage.get_todo(todo.id))
        # Try deleting again
        result = self.storage.delete_todo(todo.id)
        self.assertFalse(result)

    def test_get_nonexistent_todo(self):
        self.assertIsNone(self.storage.get_todo(9999))

    def test_update_nonexistent_todo(self):
        updated = self.storage.update_todo(9999, title="Noop")
        self.assertIsNone(updated)

if __name__ == "__main__":
    unittest.main()
