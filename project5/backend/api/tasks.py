from fastapi import APIRouter, HTTPException
from typing import List
from datetime import date
from pydantic import BaseModel

# Define the schema for response
class TodoItem(BaseModel):
    id: int
    title: str
    done: bool
    due_date: date | None = None

class TodoCreate(BaseModel):
    title: str
    done: bool = False
    due_date: date | None = None

class TodoUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None
    due_date: date | None = None

# In-memory fake storage
fake_tasks_db = [
    TodoItem(id=1, title="Buy milk", done=False, due_date=None),
    TodoItem(id=2, title="Call Alice", done=True, due_date="2024-06-15"),
]

router = APIRouter()

def get_next_id():
    if fake_tasks_db:
        return max(task.id for task in fake_tasks_db) + 1
    return 1

@router.get("/tasks", response_model=List[TodoItem])
def list_tasks():
    return fake_tasks_db

@router.post("/tasks", response_model=TodoItem, status_code=201)
def create_task(task: TodoCreate):
    new_id = get_next_id()
    todo_item = TodoItem(id=new_id, **task.dict())
    fake_tasks_db.append(todo_item)
    return todo_item

@router.delete("/tasks/{id}", status_code=204)
def delete_task(id: int):
    global fake_tasks_db
    for idx, task in enumerate(fake_tasks_db):
        if task.id == id:
            del fake_tasks_db[idx]
            return
    raise HTTPException(status_code=404, detail="Task not found")

@router.patch("/tasks/{id}", response_model=TodoItem)
def update_task(id: int, changes: TodoUpdate):
    for idx, task in enumerate(fake_tasks_db):
        if task.id == id:
            task_data = task.dict()
            update_data = changes.dict(exclude_unset=True)
            updated_task = TodoItem(**{**task_data, **update_data})
            fake_tasks_db[idx] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")
