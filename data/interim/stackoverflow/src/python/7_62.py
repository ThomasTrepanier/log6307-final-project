class Particle:
    color = (255, 255, 0)
    ID = 0

    def __init__(self, rect):
        Particle.ID += 1
        self.rect = rect

        print(self.ID)
        print(self.color)

p = Particle(None)
