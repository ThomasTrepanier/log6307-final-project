def create_bricks():
    bricks = []
    for i in range(NUM_BRICK_ROWS):
        for j in range(NUM_BRICK_COLS):
            brick = Brick(BRICK_WIDTH * j, BRICK_HEIGHT * i)  # Assuming you have a Brick class
            bricks.append(brick)
    return bricks
