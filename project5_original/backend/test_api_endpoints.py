"""
Test script for backend TODO REST API endpoints using requests.
This script tests CRUD functionality (Create, Read, Update, Delete)
of the /tasks API endpoints.

Run: Make sure the FastAPI backend is running (default: http://127.0.0.1:8000)
"""
import requests

BASE_URL = "http://127.0.0.1:8000"
TASKS_ENDPOINT = f"{BASE_URL}/tasks"

def print_section(title):
    print("\n" + "="*len(title))
    print(title)
    print("="*len(title))

def test_create_task():
    print_section("Testing POST /tasks (Create task)")
    data = {"title": "Test the API", "status": False, "due_date": "2024-12-31"}
    response = requests.post(TASKS_ENDPOINT, json=data)
    assert response.status_code == 201, response.text
    task = response.json()
    assert task["title"] == data["title"]
    assert task["status"] == data["status"]
    assert task["due_date"] == data["due_date"]
    print("Created task:", task)
    return task["id"]

def test_get_tasks():
    print_section("Testing GET /tasks (List tasks)")
    response = requests.get(TASKS_ENDPOINT)
    assert response.status_code == 200, response.text
    tasks = response.json()
    print("Current tasks:", tasks)
    return tasks

def test_patch_task(task_id):
    print_section("Testing PATCH /tasks/{id} (Update task)")
    data = {"status": True, "title": "Updated Title"}
    response = requests.patch(f"{TASKS_ENDPOINT}/{task_id}", json=data)
    assert response.status_code == 200, response.text
    task = response.json()
    assert task["id"] == task_id
    assert task["title"] == data["title"]
    assert task["status"] is True
    print("Updated task:", task)

def test_delete_task(task_id):
    print_section("Testing DELETE /tasks/{id} (Delete task)")
    response = requests.delete(f"{TASKS_ENDPOINT}/{task_id}")
    assert response.status_code == 204, response.text
    print(f"Deleted task with id={task_id}")

def test_task_lifecycle():
    task_id = test_create_task()
    _ = test_get_tasks()
    test_patch_task(task_id)
    _ = test_get_tasks()
    test_delete_task(task_id)
    tasks = test_get_tasks()
    # The test task should be gone now
    assert not any(task["id"] == task_id for task in tasks)
    print("Task lifecycle tested successfully.")

if __name__ == "__main__":
    test_task_lifecycle()
