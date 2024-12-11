from turtle import Turtle, Screen
import random

#tim = Turtle()
screen = Screen()

### Turtle race
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle_count in range(0,6):
    turtlie = Turtle(shape="turtle")
    turtlie.color(colors[turtle_count])
    turtlie.penup()
    turtlie.goto(x=-200, y=int(-125+50*turtle_count))
    all_turtles.append(turtlie)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtlie in all_turtles:
        if turtlie.xcor() >230:
            is_race_on = False
            winner = turtlie.pencolor()
            if winner == user_bet:
                print(f"Congrats!!! You've won! The winner is {winner}")
            else:
                print(f"You've lost. The winner was {winner}")
        go = random.randint(0,10)
        turtlie.forward(go)


screen.exitonclick()