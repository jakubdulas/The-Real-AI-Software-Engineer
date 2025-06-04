# Frontend - TODO List Application

This directory contains the frontend code for the web-based TODO list application. The frontend is a simple HTML + JavaScript application that interacts with the backend REST API to display and manage TODO tasks.

## Project Structure

```
frontend/
├── index.html   # Main HTML file for the app's UI
├── app.js       # JavaScript logic for fetching tasks, and handling add/delete
├── style.css    # Optional: minimal styling for the app (not required for functionality)
└── README.md    # This file
```

## Files

### index.html
- The main entry point of the frontend application.
- Sets up the structure of the page, including the task input form and the task list.
- Loads `app.js` for frontend logic.

### app.js
- Contains all application logic (see code comments for details):
  - Fetches the list of TODO tasks from the backend API (`GET /tasks`).
  - Allows users to add new tasks via the form (`POST /tasks`).
  - Allows users to delete tasks (`DELETE /tasks/{id}`).
  - Updates the DOM to reflect the current list of tasks.
- Uses `fetch` to communicate with the backend server at `http://localhost:8000` (you may need to update the URL if your backend runs elsewhere).

### style.css (optional)
- Contains minimal CSS styles for improving the appearance of the TODO app. The app will work without this file; it's only for visual enhancement.

## Usage

### Prerequisites
- You need a running backend API server (see backend/README.md for instructions).
- A modern web browser (no build tools are required).

### How to Run
1. Start your backend server (see the backend instructions).
2. Open `frontend/index.html` in your browser directly.
3. Use the form to add tasks. All tasks will be listed and can be deleted.

### Customization
- If your backend runs on a different host or port, edit the URLs in `app.js` accordingly.

## Notes
- If you open `index.html` directly from the filesystem, some browsers may block `fetch` requests to `localhost` due to CORS or file URL restrictions. If this happens, serve the frontend using a simple HTTP server. For example:

```
cd frontend
python3 -m http.server 8080
```

- Then open [http://localhost:8080/index.html](http://localhost:8080/index.html) in your browser.

---
For any issues, please refer to backend and frontend READMEs or contact the project maintainer.
