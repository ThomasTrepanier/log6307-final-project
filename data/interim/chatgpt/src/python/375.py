class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.some_data = "Initial Data"

    def display_data(self):
        print(self.some_data)


# Application
if __name__ == "__main__":
    singleton1 = Singleton()
    singleton1.display_data()  # Outputs: Initial Data

    singleton2 = Singleton()
    singleton2.some_data = "Changed Data"
    singleton2.display_data()  # Outputs: Changed Data

    # Displaying from first reference to validate singleton property
    singleton1.display_data()  # Outputs: Changed Data
    print(singleton1 is singleton2)  # Outputs: True
