from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(0,250)
        self.color("white")
        self.update_scoreboard()
    
    def increse_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write( f"Score: {self.score}", align=ALIGN, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
