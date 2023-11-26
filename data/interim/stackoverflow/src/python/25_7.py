from turtle import Turtle
import random

josh = Turtle()
josh.color('DarkRed')

def random_color()->tuple:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

josh.speed('fastest')
josh.pensize(2)
for i in range(72):
    josh.circle(100)
    josh.right(5)
    colormode(255)
    josh.pencolor(random_color())
        
screen = Screen()
screen.setup(800,800)
screen.exitonclick()
