class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Loading Configuration...")
            cls._instance = super().__new__(cls)
        return cls._instance

config1 = ConfigurationManager()
config2 = ConfigurationManager()

print(config1 == config2)