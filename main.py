from turtle import Turtle,Screen
from paddle import Paddle
from pong import Pong
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)

pong = Pong((0,0))
score = Score()
score.show_score()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
screen.listen()

screen.onkey(key="w",fun=l_paddle.go_up)
screen.onkey(key="s",fun=l_paddle.go_down)

screen.onkey(key="Up",fun=r_paddle.go_up)
screen.onkey(key="Down",fun=r_paddle.go_down)

game_on = True
while game_on:
    time.sleep(0.1)
    pong.speed("slow")
    pong.move()

    if (pong.ycor() >280) or (pong.ycor() < -280):
        pong.bounce()
    if (pong.distance(r_paddle) < 50) and pong.xcor() > 320:
        pong.bounce_x()
    if (pong.distance(l_paddle) < 50) and pong.xcor() < -320:
        pong.bounce_x()

    if pong.xcor() > 380:
        score.l_score +=1
        score.show_score()
        pong.reset_pos()
        pong.bounce_x()
        # game_on = False
    if pong.xcor() < -380:
        score.r_score +=1
        score.show_score()
        pong.reset_pos()
        pong.bounce_x()
        # game_on = False
    screen.update()

screen.exitonclick()