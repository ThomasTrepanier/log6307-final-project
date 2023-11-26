class Agent:
    def __init__(self, name, age, personality, occupation, motivation):
        self.name = name
        self.age = age
        self.personality = personality
        self.occupation = occupation
        self.motivation = motivation
        self.daily_schedule = {}

    def describe(self):
        return f"{self.name} is a {self.age} years old {self.personality} individual. {self.name}'s main motivation is {self.motivation} and currently working as a {self.occupation}."

    def set_schedule(self, schedule):
        self.daily_schedule = schedule

    def get_schedule(self):
        return self.daily_schedule


# Example of usage
eddy = Agent('Eddy Lin', 21, 'curious', 'student', 'exploring musical styles')

print(eddy.describe())

schedule = {
    "7:00": "wake up",
    "8:00": "go to library",
    "12:00": "lunch at Hobbs Cafe",
    "13:00": "walk in the park",
    "14:00": "return to library",
    "18:00": "finish library work"
}

eddy.set_schedule(schedule)

print(eddy.get_schedule())
