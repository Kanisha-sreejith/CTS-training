# WEEK-II: SQLAlchemy ORM CRUD operations example

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    grade = Column(String, nullable=False)

engine = create_engine('sqlite:///week2_example.db', echo=False)
SessionLocal = sessionmaker(bind=engine)

def setup_database():
    Base.metadata.create_all(engine)

def create_student(name: str, grade: str):
    session = SessionLocal()
    student = Student(name=name, grade=grade)
    session.add(student)
    session.commit()
    session.refresh(student)
    session.close()
    return student

def read_students():
    session = SessionLocal()
    students = session.query(Student).all()
    session.close()
    return students

def update_student(student_id: int, new_grade: str):
    session = SessionLocal()
    student = session.query(Student).filter(Student.id == student_id).first()
    if student:
        student.grade = new_grade
        session.commit()
    session.close()
    return student

def delete_student(student_id: int):
    session = SessionLocal()
    student = session.query(Student).filter(Student.id == student_id).first()
    if student:
        session.delete(student)
        session.commit()
    session.close()
    return student

if __name__ == '__main__':
    setup_database()
    s1 = create_student('Emma', 'A')
    s2 = create_student('Liam', 'B')
    print('Created:', s1.id, s1.name, s1.grade)
    print('Created:', s2.id, s2.name, s2.grade)

    students = read_students()
    print('All students:', [(s.id, s.name, s.grade) for s in students])

    update_student(s1.id, 'A+')
    print('Updated:', [(s.id, s.name, s.grade) for s in read_students()])

    delete_student(s2.id)
    print('After delete:', [(s.id, s.name, s.grade) for s in read_students()])
