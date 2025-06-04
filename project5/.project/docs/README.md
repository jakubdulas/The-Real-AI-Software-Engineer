# TODO List App – Local Setup Guide

This guide explains how to install and run both the backend API and the frontend for the TODO list web application on your local machine.

---

## 1. Backend: REST API

### Framework: FastAPI (example, adapt if using Flask or Django)

### Setup Steps

#### a. Requirements
- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)

#### b. Installation & Environment Setup

```bash
cd backend
python -m venv venv        # Create a virtual environment (optional, but recommended)
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### c. Running the Backend

```bash
uvicorn main:app --reload  # Assumes your FastAPI code is in backend/main.py
```
Backend will run by default at [http://localhost:5000](http://localhost:5000)

> For Flask:
> ```bash
> flask --app main run
> ```
> For Django:
> ```bash
> python manage.py runserver 5000
> ```

#### d. Backend API Endpoints
- `GET    /tasks`          — List all tasks
- `POST   /tasks`          — Add a new task
- `PATCH  /tasks/{id}`     — Update task
- `DELETE /tasks/{id}`     — Delete task

---

## 2. Frontend: HTML + JavaScript

#### a. Setup
No build step or extra dependencies required.

#### b. Start Frontend

```bash
cd frontend
python -m http.server 8000
```

This serves the frontend at [http://localhost:8000](http://localhost:8000).

You can now open this URL in your browser and use the TODO app UI. The frontend fetches data from the backend API.

---

## 3. Environment & URLs

- **Frontend URL:**  [http://localhost:8000](http://localhost:8000)
- **Backend API URL:** [http://localhost:5000](http://localhost:5000)
  - _If you change backend port, update API URLs in frontend code as well._

### CORS Note
If developing locally, CORS (Cross-Origin Resource Sharing) settings must allow requests from `http://localhost:8000` on the backend. This is typically handled by the backend project settings (e.g. with FastAPI's CORSMiddleware).

---

## 4. Example Project Structure

```
project/
  backend/
    main.py
    requirements.txt
  frontend/
    index.html
    app.js
  README.md
```

---

## 5. Troubleshooting

- Ensure both backend and frontend are running (separate terminals recommended).
- If you see CORS errors, double-check backend CORS configuration and port numbers.
- If you change backend or frontend ports, make sure they match in the URLs.
