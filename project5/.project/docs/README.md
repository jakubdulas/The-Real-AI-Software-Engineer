# Web-based TODO List Application

This project is a simple web-based TODO list application. The backend is provided as a REST API (with FastAPI, Flask, or Django REST Framework), and the frontend is implemented with basic HTML and JavaScript. Backend and frontend code are kept in separate directories for clarity.

---

## Prerequisites
- **Python 3.8+** (for backend)
- **pip** (Python package installer)
- **Node.js** and **npm** *[optional: only if you make changes to modern frontend tools, otherwise not required]*
- A web browser

---

## Project Structure

```
project-root/
│
├── backend/           # backend API code
├── frontend/          # HTML + JS client
├── README.md          # this file
```

---

## Backend - Local Setup and Running

1. **Navigate to `backend/`:**
   ```bash
   cd backend
   ```

2. **Create a Python virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   - If `requirements.txt` is provided:
     ```bash
     pip install -r requirements.txt
     ```
   - Otherwise, install typical dependencies for FastAPI:
     ```bash
     pip install fastapi uvicorn
     # or for Flask:
     # pip install flask
     # or for Django REST framework:
     # pip install django djangorestframework
     ```

4. **Run the backend server:**
   - For FastAPI (example):
     ```bash
     uvicorn main:app --reload
     ```
   - For Flask:
     ```bash
     export FLASK_APP=main.py     # or set FLASK_APP=main.py on Windows
     flask run
     ```
   - For Django:
     ```bash
     python manage.py runserver
     ```
   
   The backend API will be available by default at `http://127.0.0.1:8000` for FastAPI/Uvicorn, or `http://127.0.0.1:5000` for Flask, or `http://127.0.0.1:8000` for Django.

5. **API Example:**
   - Visit `http://localhost:8000/docs` (FastAPI auto-docs) or use `curl`/Postman to test the endpoints:
     ```bash
     curl http://127.0.0.1:8000/tasks
     ```

---

## Frontend - Local Setup and Running

1. **Navigate to `frontend/`:**
   ```bash
   cd ../frontend
   ```

2. **Open `index.html` in any browser** (no build step or server required unless CORS or other restrictions apply):
   - You can simply double-click `index.html` or run:
     ```bash
     python -m http.server
     # then visit http://localhost:8000 in your browser
     ```

   This static frontend will communicate with the backend API at `localhost` (ensure the backend is running).

3. **Usage:**
   - List, add, and delete tasks using the web interface.
   - The frontend uses fetch requests to call the API endpoints as described above.

---

## Example API Endpoints

- `GET     /tasks`            - List all tasks
- `POST    /tasks`            - Add a new task (`{"title": ..., "due_date": ...}`)
- `PATCH   /tasks/{id}`       - Update a task (e.g., `{ "done": true }`)
- `DELETE  /tasks/{id}`       - Delete a task

---

## Notes
- Ensure the backend and frontend run on compatible `localhost` ports, or adjust fetch URLs or use a proxy as needed.
- For development convenience you may enable CORS in the backend (for FastAPI, see [FastAPI CORS docs](https://fastapi.tiangolo.com/tutorial/cors/)).

---

## Troubleshooting
- **If tasks do not appear:** Confirm the backend server is running and accessible.
- **CORS errors in frontend:** Enable CORS in backend or use a browser extension for local development.

---

## License
MIT or as specified in the project.
