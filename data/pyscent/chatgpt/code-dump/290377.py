class Base:
    def method(self):
        print("Base method")

class Derived(Base):
    def method(self):
        super().method()
        print("Derived method")

d = Derived()
d.method()
