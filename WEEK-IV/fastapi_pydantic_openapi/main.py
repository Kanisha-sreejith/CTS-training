from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Student API Example")


class Student(BaseModel):
    name: str
    course: str
    grade: str = "A"


students = []


@app.get("/")
def read_root():
    return {"message": "Welcome to the Student API"}


@app.get("/students", response_model=list[Student])
def list_students():
    return students


@app.post("/students", response_model=Student)
def create_student(student: Student):
    students.append(student)
    return student


@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]


@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student: Student):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")
    students[student_id] = student
    return student


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")
    students.pop(student_id)
    return {"message": "Student deleted"}
