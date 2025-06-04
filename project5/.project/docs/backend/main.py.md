# backend/main.py

This file implements a RESTful backend API for a TODO list web application using FastAPI. The API enables clients to create, read, update, and delete TODO items. The module also handles Cross-Origin Resource Sharing (CORS) to allow connections from the local frontend.

## FastAPI Application Overview
- **Framework:** FastAPI
- **CORS:** Configured to allow requests from `http://localhost:8000`
- **Data Storage:** In-memory list (no persistence)

## Data Models

### Task
Represents a TODO item.
- `id` (int): Unique task identifier.
- `title` (str): Task title.
- `done` (bool): Status of completion (default: False).
- `due_date` (date, optional): Optional due date for the task.

### TaskCreate
Model for creating new tasks (client request body).
- `title` (str): Task title (required).
- `done` (bool): Completion status (default: False).
- `due_date` (date, optional): Due date.

### TaskUpdate
Model for updating part of a task (client request body).
- All fields are optional for partial updates.

## Key Variables
- `tasks` (List[Task]): Stores all TODO items in memory.
- `task_id_counter` (int): Auto-incrementing counter to assign unique IDs.

## API Endpoints

### `GET /tasks`
Returns a list of all TODO tasks.

### `POST /tasks`
Creates a new task from the provided JSON body (TaskCreate).
Increments the id counter and adds the task to the list.
Returns the created "Task" object.

### `PATCH /tasks/{task_id}`
Partially updates an existing task identified by `task_id` using provided fields. Returns the updated "Task" object. Returns 404 if task not found.

### `DELETE /tasks/{task_id}`
Deletes a task by `task_id`. Returns status 204 on success. Returns 404 if task not found.

## CORS
CORS middleware is set up to allow requests from the local frontend app at port 8000 (adjust as needed).

## Docstrings and Code Annotations
All route handlers and models include Python docstrings for clarity and maintainability, explaining the purpose, arguments, and return values.
