from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Light:
    def on(self):
        print("Light ON")


class LightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


if __name__ == "__main__":
    light = Light()
    command = LightCommand(light)
    command.execute()