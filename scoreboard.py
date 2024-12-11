from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(-220, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score = {self.score}", align="center", font=("Courier", 20, "normal"))

    def increase(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align="center", font=("Courier", 24, "normal"))