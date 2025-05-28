from fastapi import FastAPI, Depends
from sqlalchemy import Column, Integer, String, Boolean, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import List, Optional
from datetime import date
from pydantic import BaseModel

# SQLAlchemy setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./todo.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# TODO model (DB)
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    status = Column(
        Boolean, default=False, nullable=False
    )  # False = not done, True = done
    due_date = Column(Date, nullable=True)


# Pydantic Schemas
class TodoCreate(BaseModel):
    title: str
    status: bool = False
    due_date: Optional[date] = None


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    status: Optional[bool] = None
    due_date: Optional[date] = None


class TodoItem(BaseModel):
    id: int
    title: str
    status: bool
    due_date: Optional[date] = None

    class Config:
        orm_mode = True


# App setup
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create tables if run directly
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)


# GET /tasks endpoint
def _get_all_tasks(db: Session):
    return db.query(Todo).all()


@app.get("/tasks", response_model=List[TodoItem])
def get_tasks(db: Session = Depends(get_db)):
    tasks = _get_all_tasks(db)
    return tasks


# POST /tasks endpoint
def _create_task(db: Session, todo: TodoCreate):
    new_task = Todo(title=todo.title, status=todo.status, due_date=todo.due_date)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@app.post("/tasks", response_model=TodoItem, status_code=201)
def create_task(todo: TodoCreate, db: Session = Depends(get_db)):
    task = _create_task(db, todo)
    return task


# PATCH /tasks/{id} endpoint
from fastapi import HTTPException


def _update_task(db: Session, task_id: int, task_update: TodoUpdate):
    db_task = db.query(Todo).filter(Todo.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    data = task_update.dict(exclude_unset=True)
    for field, value in data.items():
        setattr(db_task, field, value)
    db.commit()
    db.refresh(db_task)
    return db_task


@app.patch("/tasks/{id}", response_model=TodoItem)
def update_task(id: int, task_update: TodoUpdate, db: Session = Depends(get_db)):
    return _update_task(db, id, task_update)


# DELETE /tasks/{id} endpoint
def _delete_task(db: Session, task_id: int):
    db_task = db.query(Todo).filter(Todo.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return {"detail": "Task deleted"}


@app.delete("/tasks/{id}", status_code=204)
def delete_task(id: int, db: Session = Depends(get_db)):
    _delete_task(db, id)
    return None
