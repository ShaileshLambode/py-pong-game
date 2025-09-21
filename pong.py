from turtle import Turtle
from turtledemo.paint import switchupdown


class Pong(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x_cor = self.xcor() +self.x_move
        y_cor = self.ycor() +self.y_move
        self.goto(x_cor,y_cor)

    def bounce(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1

    def reset_pos(self):
        self.goto(0, 0)