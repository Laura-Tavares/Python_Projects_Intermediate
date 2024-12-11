from turtle import Turtle

class Racer(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("chartreuse4")
        self.penup()
        self.setheading(90)
        self.goto(x=0,y=-280)
        
    def move(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def refresh(self):
        self.setheading(90)
        self.goto(x=0, y=-280)