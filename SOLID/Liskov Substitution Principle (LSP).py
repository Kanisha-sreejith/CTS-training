class Bird:
    def move(self):
        print("Bird is moving")


class Sparrow(Bird):
    def move(self):
        print("Sparrow is flying")


class Penguin(Bird):
    def move(self):
        print("Penguin is swimming")


if __name__ == "__main__":
    bird_one = Sparrow()
    bird_two = Penguin()

    bird_one.move()
    bird_two.move()