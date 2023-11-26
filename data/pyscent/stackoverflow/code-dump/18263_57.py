from turtle import Turtle, Screen
from random import randrange

def run(turtle):
    turtle.forward(5)

    if turtle.xcor() < half_width:
        screen.ontimer(lambda: run(turtle), randrange(20, 150))

screen = Screen()

half_width = screen.window_width() / 2
lane_width = 20

for order, color in enumerate(['red', 'green', 'blue']):
    turtle = Turtle('turtle')
    turtle.speed('fastest')
    turtle.color(color)
    turtle.penup()

    turtle.goto(-half_width, (order | 1) * lane_width)
    lane_width *= -1
    run(turtle)

screen.exitonclick()
