from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def start(self):
        pass


class PetrolEngine(Engine):
    def start(self):
        print("Petrol Engine Started")


class Car:
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        self.engine.start()
        print("Car is Running")


if __name__ == "__main__":
    engine = PetrolEngine()
    car = Car(engine)
    car.drive()