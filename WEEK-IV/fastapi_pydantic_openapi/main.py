from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Student API")


class Student(BaseModel):
    name: str
    course: str


students = []


@app.get("/")
def home():
    return {"message": "Welcome to the Student API"}


@app.get("/students")
def list_students():
    return students


@app.post("/students")
def add_student(student: Student):
    students.append(student)
    return student
