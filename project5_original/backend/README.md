# TODO List Backend

This is the backend REST API for the TODO list application, built with FastAPI.

## Setup Instructions

1. **Install Python 3.8+**
2. (Recommended) Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the API server:**
   ```bash
   uvicorn main:app --reload
   ```
   Access the interactive docs at: http://127.0.0.1:8000/docs
