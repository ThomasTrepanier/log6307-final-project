# Modify the Brick class to accept a color parameter
class Brick:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, self.w, self.h))

# Create bricks
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]  # Red, green, blue, yellow
bricks = []
for i in range(4):
    row = [Brick(x, 50 + i * 25, 70, 20, colors[i]) for x in range(0, WINDOW_WIDTH, 75)]
    bricks.extend(row)
