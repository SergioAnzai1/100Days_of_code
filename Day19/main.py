from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_fowards():
    tim.forward(10)
    
def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_rigth():
    tim.right(10)

screen.listen()
screen.onkey(key="w",fun=move_fowards)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="d",fun=turn_rigth)
screen.onkey(key="c",fun=tim.reset)

screen.exitonclick()