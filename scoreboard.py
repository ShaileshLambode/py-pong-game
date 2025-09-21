from turtle import Turtle

FONT=("Arial", 24 ,"bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0

    def show_score(self):
        self.clear()
        self.goto(-100,250)
        self.write(self.l_score,align="center",font=FONT)
        self.goto(100,250)
        self.write(self.r_score,align="center",font=FONT)




