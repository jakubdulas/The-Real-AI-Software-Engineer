from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

app = FastAPI()

# Allow CORS for local frontend (adjust if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Task(BaseModel):
    id: int
    title: str = Field(..., example="Buy groceries")
    done: bool = False
    due_date: Optional[date] = None


class TaskCreate(BaseModel):
    title: str = Field(..., example="Buy groceries")
    done: bool = False
    due_date: Optional[date] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None
    due_date: Optional[date] = None


tasks: List[Task] = []
task_id_counter = 1


@app.get("/tasks", response_model=List[Task])
def list_tasks():
    return tasks


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    global task_id_counter
    new_task = Task(id=task_id_counter, **task.dict())
    tasks.append(new_task)
    task_id_counter += 1
    return new_task


@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskUpdate):
    for idx, t in enumerate(tasks):
        if t.id == task_id:
            updated_fields = task_update.dict(exclude_unset=True)
            updated_task = t.copy(update=updated_fields)
            tasks[idx] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    global tasks
    for idx, t in enumerate(tasks):
        if t.id == task_id:
            del tasks[idx]
            return
    raise HTTPException(status_code=404, detail="Task not found")
