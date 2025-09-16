from fastapi import FastAPI, HTTPException  # HTTPException [FastAPI error handler for HTTP responses]
from pydantic import BaseModel              # BaseModel [Pydantic class for input validation]
import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi.middleware.cors import CORSMiddleware  # CORS [middleware to allow cross-origin requests]


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # allow all HTTP methods
    allow_headers=["*"],  # allow all headers
)

# Connect to your local Postgres database
conn = psycopg2.connect(
    host="localhost",
    database="todo_app",
    user="your_username",  # replace with your actual username
    password="your_password",  # replace with your actual password
    cursor_factory=RealDictCursor
)

# Define input schema using Pydantic
class Task(BaseModel):  # Task [Pydantic model to validate incoming JSON]
    title: str
    completed: bool

@app.get("/tasks")
def get_tasks():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM tasks;")
        tasks = cur.fetchall()
    return tasks

@app.post("/tasks")
def create_task(task: Task):  # task: Task [validated input object with title and completed fields]
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO tasks (title, completed) VALUES (%s, %s) RETURNING id;",
                (task.title, task.completed)  # parameterized query to prevent SQL injection
            )
            new_id = cur.fetchone()["id"]
            conn.commit()  # persist changes to database
        return {"id": new_id, "title": task.title, "completed": task.completed}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # return error if insertion fails
    

# Existing endpoints omitted for brevity...

@app.delete("/tasks/{task_id}")  # DELETE [HTTP method to remove resources]
def delete_task(task_id: int):  # task_id: int [path parameter representing the task's ID]
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM tasks WHERE id = %s RETURNING id;", (task_id,))
            deleted = cur.fetchone()
            conn.commit()
        if not deleted:
            raise HTTPException(status_code=404, detail="Task not found")
        return {"status": "deleted", "id": deleted["id"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    

class TaskUpdate(BaseModel):  # TaskUpdate [Pydantic model for updating task fields]
    completed: bool

@app.put("/tasks/{task_id}")  # PUT [HTTP method to update resources]
def update_task(task_id: int, update: TaskUpdate):  # update: TaskUpdate [validated input with new completed value]
    try:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE tasks SET completed = %s WHERE id = %s RETURNING id, title, completed;",
                (update.completed, task_id)
            )
            updated = cur.fetchone()
            conn.commit()
        if not updated:
            raise HTTPException(status_code=404, detail="Task not found")
        return updated  # returns updated task dictionary
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
