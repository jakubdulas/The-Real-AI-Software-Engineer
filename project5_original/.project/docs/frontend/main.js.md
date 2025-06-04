# frontend/main.js

This file contains the JavaScript logic for the frontend of the TODO list web application.

## Key Functionalities
- **Fetch tasks from backend** (`fetchTasks`) and display them in the task list when the page is loaded.
- **Add new tasks** to the backend API via the form (`addTask`).
- **Render tasks**: Dynamically displays all TODO items in the list (`renderTasks`).

## API URL
- `API_URL` points to the backend API endpoint for tasks. Adjust the port if your backend runs elsewhere.
- Example: `'http://localhost:8001/tasks'` (update to match your backend port).

## Main Components & Comments

### Event Listener: DOMContentLoaded
Initializes handlers when the DOM is ready:
- Fetches and displays all tasks.
- Binds a submit event listener to the Add Task form:
  - Prevents default form submission.
  - Adds the new task to the backend if the input is non-empty.

### fetchTasks()
- Sends GET request to backend `/tasks` endpoint.
- Receives all tasks and passes them to `renderTasks`.
- Handles fetch errors and logs to console.

### addTask(title)
- Sends POST request to backend with JSON body containing `title`.
- If successful, re-fetches task list to update the UI.
- Shows an alert if task creation fails.

### renderTasks(tasks)
- Receives array of tasks from backend.
- Empties the current task list.
- Iterates through all tasks and creates `<li>` elements for display.
    - Task titles are displayed.
    - Potential to add delete button or completion toggle (not included here).

## Comments and Future Improvements
- Tasks are displayed with their title only; marking as done and deleting requires further implementation.
- Add more comments if extending with update/delete features or more detailed status handling.
- Minimal error handling is provided; customize as necessary for your application's needs.
