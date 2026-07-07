class Student:
    def __init__(self, builder):
        self.name = builder.name
        self.age = builder.age

    def display(self):
        print(f"{self.name} {self.age}")

    class StudentBuilder:
        def __init__(self):
            self.name = None
            self.age = None

        def set_name(self, name):
            self.name = name
            return self

        def set_age(self, age):
            self.age = age
            return self

        def build(self):
            return Student(self)


if __name__ == "__main__":
    student = Student.StudentBuilder().set_name("Kanisha").set_age(21).build()
    student.display()