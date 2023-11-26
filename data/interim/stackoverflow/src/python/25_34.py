import turtle
import math

def circle2(radius,extent=360,steps=360):
    if extent<360 and steps==360:
        steps=extent
    
    theta=extent/steps
    step_size=2*radius*math.sin(math.radians(theta/2))
    turtle.left(theta/2)
    turtle.forward(step_size)
    for i in range(1,steps):
        turtle.left(theta)
        turtle.forward(step_size)
    
    turtle.left(theta/2)
    

turtle.hideturtle()
turtle.speed(0)
turtle.getscreen().tracer(False)

circle2(50)
circle2(100,180)
turtle.up()
turtle.home()
turtle.down()
circle2(130)
circle2(130,360,10)

turtle.update()
turtle.mainloop()
