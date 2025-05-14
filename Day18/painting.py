import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.speed("fastest")

def random_color():    
    colors = [
        (224, 233, 227),
        (207, 160, 81),
        (56, 88, 130),
        (144, 91, 41),
        (139, 27, 48),
        (221, 207, 108),
        (134, 177, 201),
        (157, 47, 85),
        (43, 54, 105),
        (170, 159, 41),
        (130, 189, 144),
        (83, 20, 43),
        (39, 43, 64),
        (185, 95, 108),
        (189, 140, 166),
        (86, 122, 180),
        (59, 40, 31),
        (89, 157, 93),
        (80, 153, 165),
        (194, 80, 73),
        (45, 75, 77),
        (160, 201, 219),
        (54, 129, 127),
        (80, 75, 44),
        (218, 176, 186),
        (46, 74, 73),
        (170, 206, 167),
        (221, 180, 168),
        (179, 188, 211),
        (143, 37, 35),
        (43, 63, 62),
    ]
    color = random.choice(colors)
    return color

def go_to_start_position():

    tim.back(300)
    tim.left(90)
    tim.back(200)
    tim.right(90)

def make_dots():
    for _ in range (10):
        tim.forward(50)
        tim.dot(20, random_color())
        
def next_line():
    tim.back(500)
    tim.left(90)
    tim.forward(50)
    tim.right(90)

# main code 
tim.penup()
go_to_start_position() 
for _ in range(10):
    make_dots()
    next_line()

screen = t.Screen()
screen.exitonclick()
