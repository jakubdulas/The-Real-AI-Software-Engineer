# TODO List Backend API

This is the backend FastAPI application for the TODO list app.

## Requirements
- Python 3.8+
- FastAPI
- Uvicorn

## Setup (local)

1. **Navigate to the backend directory:**

    ```sh
    cd backend
    ```

2. **(Recommended) Create & activate a virtual environment:**

    On Unix/Mac:
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```
    On Windows:
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the development server:**

    ```sh
    uvicorn main:app --reload
    ```

5. **Visit your API:**

    - API root: http://127.0.0.1:8000/
    - Swagger docs: http://127.0.0.1:8000/docs
