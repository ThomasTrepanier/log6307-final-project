class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Usage:
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 == singleton2)  # Outputs: True, both point to the same instance.
