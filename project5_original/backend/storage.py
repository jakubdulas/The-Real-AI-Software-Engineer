"""In-memory storage for TODO items.

This module provides an in-memory storage class for TODO items with basic CRUD operations.
"""
from typing import Optional, List, Dict, Any
from datetime import date

class TodoItem:
    """Data class representing a TODO item."""
    def __init__(self, id: int, title: str, status: bool = False, due_date: Optional[date] = None):
        """Initializes a TodoItem object.

        Args:
            id: Unique identifier for the item.
            title: The task description.
            status: If True, the task is done.
            due_date: Optional due date for the task.
        """
        self.id = id
        self.title = title
        self.status = status
        self.due_date = due_date

    def to_dict(self) -> Dict[str, Any]:
        """Returns a dictionary representation of the TODO item."""
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "due_date": self.due_date.isoformat() if self.due_date else None
        }

class TodoStorage:
    """Basic in-memory storage and CRUD operations for TODO items."""
    def __init__(self):
        """Initializes the storage with an empty list and next id."""
        self._todos: List[TodoItem] = []
        self._next_id = 1

    def list_todos(self) -> List[TodoItem]:
        """Gets the list of all TODO items.

        Returns:
            List[TodoItem]: All TODO items in storage.
        """
        return list(self._todos)

    def add_todo(self, title: str, status: bool = False, due_date: Optional[date] = None) -> TodoItem:
        """Adds a new TODO item to the list.

        Args:
            title: The task description.
            status: If True, the task is done. Defaults to False.
            due_date: Optional due date.
        Returns:
            TodoItem: The created TODO item.
        """
        todo = TodoItem(id=self._next_id, title=title, status=status, due_date=due_date)
        self._todos.append(todo)
        self._next_id += 1
        return todo

    def get_todo(self, todo_id: int) -> Optional[TodoItem]:
        """Retrieves a TODO item by its ID.

        Args:
            todo_id: The id of the TODO item.
        Returns:
            TodoItem, or None if not found.
        """
        for todo in self._todos:
            if todo.id == todo_id:
                return todo
        return None

    def update_todo(self, todo_id: int, title: Optional[str] = None, status: Optional[bool] = None, due_date: Optional[date] = None) -> Optional[TodoItem]:
        """Updates a TODO item with specified fields.

        Args:
            todo_id: The id of the TODO item.
            title: New task title, if provided.
            status: New status, if provided.
            due_date: New due date, if provided.
        Returns:
            The updated TodoItem, or None if not found.
        """
        todo = self.get_todo(todo_id)
        if todo is None:
            return None
        if title is not None:
            todo.title = title
        if status is not None:
            todo.status = status
        if due_date is not None:
            todo.due_date = due_date
        return todo

    def delete_todo(self, todo_id: int) -> bool:
        """Deletes a TODO item by ID.

        Args:
            todo_id: The id of the TODO item to delete.
        Returns:
            True if deleted, False if not found.
        """
        for i, todo in enumerate(self._todos):
            if todo.id == todo_id:
                del self._todos[i]
                return True
        return False
