class MyContext:
    def __init__(self):
        self.trace = []

    def add_trace(self, info):
        self.trace.append(info)

    def get_trace(self):
        return self.trace
