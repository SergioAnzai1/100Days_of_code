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

direction = [0, 90, 180, 270]
tim.shapesize(0.1, 0.1, 0.1)
tim.pensize(15)
tim.speed("fastest")

for _ in range(1000):
    tim.pencolor(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))

screen = t.Screen()
screen.exitonclick()
