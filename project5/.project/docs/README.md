# Web-based TODO List Application

This is a simple web-based TODO list app featuring a RESTful backend API and a minimal frontend. The project is structured into two main directories:

- `backend/` – FastAPI-powered REST API for managing tasks
- `frontend/` – HTML/JavaScript frontend that interacts with the backend API

---

## Prerequisites

- **Python 3.7+** (for backend)
- **pip** (Python package manager)
- **(Optional) Node.js/any HTTP server** (for serving static frontend files if desired)

---

## Backend Setup and Running Instructions

1. **Navigate to the backend directory:**
    ```bash
    cd backend
    ```
2. **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use: venv\Scripts\activate
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(If `requirements.txt` is missing, run: `pip install fastapi uvicorn`)*
4. **Start the backend server:**
    ```bash
    uvicorn main:app --reload
    ```
    By default, the backend will be available at `http://127.0.0.1:8000/`.

---

## Frontend Setup and Running Instructions

There are two options to run the frontend:

### 1. Open Directly in Browser

1. Navigate to `frontend/`
2. Open `index.html` in your web browser (double-click or right-click open)
3. **Note:** For some browsers, direct fetch requests to the backend may be blocked due to CORS or file restrictions. If this happens, use option 2 below.

### 2. Serve via Simple HTTP Server

**Using Python's built-in HTTP server:**

```bash
cd frontend
python -m http.server 8080
```
Then visit [http://localhost:8080](http://localhost:8080) in your browser. This avoids most local file access issues.

**Or use any other static file server (e.g., Node.js `http-server`, `live-server`, etc.)**

---

## Configuration Notes

- By default, the frontend expects the backend API to run at `http://127.0.0.1:8000`.
- If your backend uses a different host/port, update the API base URL in the frontend JavaScript (`frontend/app.js`).
- Make sure both the backend and frontend are running for full functionality.

---

## Directory Structure

```
project-root/
├── backend/
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── app.js
│   └── style.css
└── README.md
```

---

## Support & Troubleshooting

- Ensure you have the correct Python and pip version installed
- If you encounter CORS issues, consider enabling CORS in your FastAPI backend with the [CORSMiddleware](https://fastapi.tiangolo.com/tutorial/cors/)
- If you need help, reference comments in the code and documentation in each subdirectory.
