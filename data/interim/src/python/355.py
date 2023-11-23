class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        pass

class NonFlyingBird(Bird):
    pass

class Sparrow(FlyingBird):
    def fly(self):
        print("Sparrow can fly.")

class Ostrich(NonFlyingBird):
    pass
