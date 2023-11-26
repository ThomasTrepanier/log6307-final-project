class Person:

    def __init__(self, name):
        self.name = name

    def get_a_job(self):
        self.job = "Janitor"
        print(f"{self.name} now has a job!")

p1 = Person("Tom")
p2 = Person("Bob")

p1.get_a_job()
print(p1.job)

print(p2.job)
