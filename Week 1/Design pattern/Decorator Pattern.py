from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass


class SimpleCoffee(Coffee):
    def cost(self):
        print("Coffee Cost = 100")


class MilkDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        self.coffee.cost()
        print("Milk Added")


if __name__ == "__main__":
    coffee = MilkDecorator(SimpleCoffee())
    coffee.cost()