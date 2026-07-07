from abc import ABC, abstractmethod


class Keyboard(ABC):
    @abstractmethod
    def type(self):
        pass


class WiredKeyboard(Keyboard):
    def type(self):
        print("Typing using Wired Keyboard")


class WirelessKeyboard(Keyboard):
    def type(self):
        print("Typing using Wireless Keyboard")


class Computer:
    def __init__(self, keyboard):
        self.keyboard = keyboard

    def work(self):
        self.keyboard.type()


if __name__ == "__main__":
    keyboard = WirelessKeyboard()
    computer = Computer(keyboard)
    computer.work()