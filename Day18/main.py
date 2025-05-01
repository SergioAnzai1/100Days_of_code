# import turtle
# tim = turtle.Turtle()

# from turtle import * (nao se usa, porque deixa o codigo confudo de ler)

# Alias name
# import turtle as t
# tim = t.Turtle()

# downloading modules
# exemple import heroes
# heroes are't in the python basic package
# in terminal type "pip install (package_name)"


from turtle import Turtle, Screen
from random import choice


def random_color():
    colors = [
        "red",
        "blue",
        "black",
        "orange",
        "green",
        "gray",
        "pink",
        "purple",
    ]
    color = choice(colors)
    return color


tim = Turtle()
tim.shape("blank")

tim.penup()
tim.back(100)
tim.left(90)
tim.forward(200)
tim.right(90)
tim.pendown()

for i in range(3, 10):
    for j in range(i):
        tim.pencolor(random_color())
        tim.forward(150)
        tim.right(360 / i)

screen = Screen()
screen.exitonclick()
