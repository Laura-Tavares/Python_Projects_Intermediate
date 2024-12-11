from turtle import Turtle
import random

COLORS = ["IndianRed3", "LightSalmon1", "LightGoldenrod3", "DarkSeaGreen", "SkyBlue2", "violet"]
INITIAL_SPEED = 5
EXTRA_SPEED = 10

class Cars:

    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            random_y = random.randint(-240,250)
            new_car.goto(x=300,y=random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(INITIAL_SPEED)

    def increase_speed(self):
        for car in self.all_cars:
            new_speed = car.speed() + EXTRA_SPEED
            car.forward(new_speed)