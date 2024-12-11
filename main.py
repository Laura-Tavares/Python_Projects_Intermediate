from turtle import Screen, Turtle

import scoreboard
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("snow2")
screen.title("Laura's Pong Game!")
screen.tracer(0)

r_paddle = Paddle(350,0, "SlateBlue4")
l_paddle = Paddle(-350,0, "VioletRed4")
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_wall()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 or
            ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_paddle()

    if ball.xcor() >= 380:
        ball.refresh()
        score.update_left_score()

    if ball.xcor() <= -380:
        ball.refresh()
        score.update_right_score()



        #game_is_on = False
        #screen.write(arg="GAME OVER", align="center", font=("Courier", 24, "normal"))

screen.exitonclick()