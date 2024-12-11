from turtle import Screen, Turtle
from racer import Racer
from scoreboard import Score
from cars import Cars
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("snow2")
screen.title("Turtle Race")
screen.tracer(0)
t_racer = Racer()
score = Score()
car_manager = Cars()

screen.listen()
screen.onkey(t_racer.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(t_racer) < 20:
            score.game_over()
            game_is_on = False

    if t_racer.ycor() >= 280:
        t_racer.refresh()
        score.increase()
        car_manager.increase_speed()

screen.exitonclick()