# Imports
from typing import Optional, Task

from fastapi import FastAPI
# BDD:
from pydantic import BaseModel


# Use BaseModel
class Task(BaseModel):

    name: str
    due_date: str
    description: str

app = FastAPI(title="Todo API")

# Create, Read, Update, Delete
store_tasks = []

# Create Task
@app.post('/task/')
async def create_task(task: Task):
    store_tasks.append(task)
    return task

# Fetch the list of tasks
@app.get('/task/', response_model=Task[Task])
async def get_all_tasks():
    return store_tasks

# Display Task Exception Not Found
@app.get('/task/{id}')
async def get_task(id: int):

    try:

        return store_tasks[id]

    except:

        raise HTTPException(status_code=404, detail="Task Not Found")

# Update Task Except Not Found
@app.put('/task/{id}')
async def update_task(id: int, task: Task):

    try:

        store_tasks[id] = task
        return store_tasks[id]

    except:

        raise HTTPException(status_code=404, detail="Task Not Found")

# Delete Tasks Except Not Found
@app.delete('/task/{id}')
async def delete_task(id: int):

    try:

        obj =store_tasks[id]
        store_tasks.pop(id)
        return obj
# pop() - Removes the element at the specified position


    except:

        raise HTTPException(status=404, detail="Task Not Found")