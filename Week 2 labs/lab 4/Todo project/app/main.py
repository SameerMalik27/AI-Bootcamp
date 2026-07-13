from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

todos = []
id_counter = 1


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str
    completed: bool


@app.get("/")
def home():
    return {"message": "Welcome to Todo API"}


@app.post("/todos")
def create_task(task: TaskCreate):
    global id_counter

    new_task = {
        "id": id_counter,
        "title": task.title,
        "completed": False
    }

    todos.append(new_task)
    id_counter += 1

    return new_task


@app.get("/todos")
def get_tasks():
    return todos


@app.get("/todos/{id}")
def get_task(id: int):

    for task in todos:
        if task["id"] == id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/todos/{id}")
def update_task(id: int, task_update: TaskUpdate):

    for task in todos:

        if task["id"] == id:

            task["title"] = task_update.title
            task["completed"] = task_update.completed

            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/todos/{id}")
def delete_task(id: int):

    for task in todos:

        if task["id"] == id:

            todos.remove(task)

            return {"message": "Task deleted successfully"}

    raise HTTPException(status_code=404, detail="Task not found")