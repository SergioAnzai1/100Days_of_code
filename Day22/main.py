from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down")



game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move(False)
    
    #detect colision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #detect colision with rigth paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
        
    #detect if ball pass the right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    #detect if ball pass the left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        
screen.exitonclick()
    






# players
# ball
# score