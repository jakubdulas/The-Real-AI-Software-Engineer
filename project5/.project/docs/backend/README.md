# Backend (TODO List App)

This directory contains the backend REST API for the TODO list application, implemented using FastAPI.

## Structure

- `main.py` — Entry point for the FastAPI application.
- `api/tasks.py` — Contains the API routes and in-memory storage logic for TODO tasks.

## API Endpoints

Base URL: `http://localhost:8000`

### GET `/tasks`
- **Description:** Retrieve the list of all tasks.
- **Response:** `200 OK`, returns a list of tasks.

### POST `/tasks`
- **Description:** Create a new task.
- **Body:**
  - `title` (string, required)
  - `done` (boolean, optional, default false)
  - `due_date` (string, optional, format: YYYY-MM-DD)
- **Response:** `201 Created`, returns the created task.

### PATCH `/tasks/{id}`
- **Description:** Update fields of a task by `id`.
- **Body:** Any subset of task fields (`title`, `done`, `due_date`).
- **Response:** `200 OK`, returns the updated task. `404` if not found.

### DELETE `/tasks/{id}`
- **Description:** Delete the task by `id`.
- **Response:** `204 No Content`. `404` if not found.

## Running locally

### Prerequisites
- Python 3.9+
- pip

### Installation & Run
1. (Optional) Create and activate a Python virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
2. Install dependencies:
   ```sh
   pip install fastapi uvicorn
   ```
3. Start the API server:
   ```sh
   uvicorn main:app --reload
   ```
4. Visit [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive API documentation (Swagger UI).

---

The backend uses an **in-memory list** as its data store—tasks are lost when the server stops.
