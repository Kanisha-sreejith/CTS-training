from abc import ABC, abstractmethod


class MobileCharger(ABC):
    @abstractmethod
    def charge(self):
        pass


class AndroidCharger(MobileCharger):
    def charge(self):
        print("Android Charging")


class IPhone:
    def lightning_charge(self):
        print("iPhone Charging")


class Adapter(MobileCharger):
    def __init__(self):
        self.iphone = IPhone()

    def charge(self):
        self.iphone.lightning_charge()


if __name__ == "__main__":
    charger = Adapter()
    charger.charge()