from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("SteelBlue4")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.score_top()
        self.update_score()

    def score_top(self):
        self.goto(0, 260)
        self.write(arg="Score", align="center", font=("Calibri", 24, "normal"))

    def update_score(self):
        self.clear()
        self.goto(60, 230)
        self.write(arg=f"{self.right_score}", align="center",font=("Calibri", 30, "normal"))
        self.goto(-60, 230)
        self.write(arg=f"{self.left_score}", align="center", font=("Calibri", 30, "normal"))

    def update_right_score(self):
        self.right_score += 1
        self.clear()
        self.update_score()
        
    def update_left_score(self):
        self.left_score += 1
        self.clear()
        self.update_score()