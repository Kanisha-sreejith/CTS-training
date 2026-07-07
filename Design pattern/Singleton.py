class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def show(self):
        print("Singleton Object")


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    s1.show()
    print(s1 is s2)