from abc import ABC, abstractmethod


class Internet(ABC):
    @abstractmethod
    def connect(self):
        pass


class RealInternet(Internet):
    def connect(self):
        print("Connected to Internet")


class ProxyInternet(Internet):
    def __init__(self):
        self.internet = RealInternet()

    def connect(self):
        print("Checking Security")
        self.internet.connect()


if __name__ == "__main__":
    internet = ProxyInternet()
    internet.connect()