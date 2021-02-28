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
        rand_heading = random.randrange(90, 270, 10)  # Angle
        # rand_heading = 210
        self.setheading(rand_heading)

    def wall_col_top(self):
        heading = self.heading()
        heading += (180 - heading) * 2
        self.setheading(heading)

    def wall_col_bot(self):
        heading = self.heading()
        step = 360 - self.heading()
        heading -= (180 - step) * 2
        self.setheading(heading)
