from turtle import Turtle, Screen
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("slow")
        self.setpos(0, 0)
        self.set_start_heading()

    def set_start_heading(self):
        rand_heading = random.randint(90, 270)  # Angle
        self.setheading(rand_heading)
