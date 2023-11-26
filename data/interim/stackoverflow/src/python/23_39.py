class NotRandom:
    def __init__(self):
        self.numbers = np.arange(1,10.5,0.5)
        self.last_index = -1

    def nrng(self):
        self.last_index += 1
        if self.last_index < len(self.numbers):
            return self.numbers[self.last_index]
        # else:
        return None

# Create an object. Then create an alias to its method
nrng = NotRandom().nrng 
