from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class Subscriber(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received: {message}")


class YouTubeChannel:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, observer):
        self.subscribers.append(observer)

    def notify_subscribers(self, message):
        for observer in self.subscribers:
            observer.update(message)


if __name__ == "__main__":
    channel = YouTubeChannel()
    channel.subscribe(Subscriber("Alice"))
    channel.subscribe(Subscriber("Bob"))
    channel.notify_subscribers("New Video Uploaded")