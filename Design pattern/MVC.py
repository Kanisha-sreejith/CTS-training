class Student:
    def __init__(self, name):
        self.name = name


class StudentView:
    def display(self, student):
        print(student.name)


class StudentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_view(self):
        self.view.display(self.model)


if __name__ == "__main__":
    student = Student("Kanisha")
    view = StudentView()
    controller = StudentController(student, view)
    controller.update_view()