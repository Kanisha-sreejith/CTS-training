class Circle:
    def draw(self):
        print("Drawing Circle")

class Rectangle:
    def draw(self):
        print("Drawing Rectangle")

class ShapeFactory:
    def create_shape(self, shape):
        if shape == "circle":
            return Circle()
        elif shape == "rectangle":
            return Rectangle()
        else:
            return None

factory = ShapeFactory()

shape = factory.create_shape("circle")
shape.draw()