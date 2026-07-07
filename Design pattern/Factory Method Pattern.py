from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def drive(self):
        print("Driving Car")


class Bike(Vehicle):
    def drive(self):
        print("Driving Bike")


class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type.lower() == "car":
            return Car()
        return Bike()


if __name__ == "__main__":
    vehicle = VehicleFactory.get_vehicle("car")
    vehicle.drive()