class NRNG:
    def __init__(self):
        self.numbers = range(10)
        self.state = -1
    def __call__(self):
        self.state += 1
        return self.numbers[self.state]
        
nrng = NRNG()


for i in range(10):
    print(nrng())
