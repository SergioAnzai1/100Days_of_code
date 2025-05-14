import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_rgb = (r, g, b)
    return random_rgb

tim.shapesize(0.1, 0.1, 0.1)
tim.pensize(1)
tim.speed("fastest")

for _ in range(0, 360, 5):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.setheading(_)

screen = t.Screen()
screen.exitonclick()
