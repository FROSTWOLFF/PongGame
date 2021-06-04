from turtle import Turtle, Screen
import time
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
        # direction = random.choice(["left", "right"])
        # if direction == "left":
        #
        # elif direction == "right":
        #     rand_heading = random.randrange(60, -60, 10)  # Angle
        rand_heading = random.randrange(120, 240, 10)  # Angle
        self.setheading(rand_heading)

    def reset(self):
        self.set_start_heading()
        self.setpos(0, 0)

    def wall_col_top(self):
        heading = self.heading()
        heading += (180 - heading) * 2
        self.setheading(heading)

    def wall_col_bot(self):
        heading = self.heading()
        step = 360 - self.heading()
        heading -= (180 - step) * 2
        self.setheading(heading)

    def bar_col_left(self):
        heading = self.heading()
        heading = 180 - heading
        self.setheading(heading)

    def bar_col_right(self):
        heading = self.heading()
        heading += (90 - heading) * 2
        self.setheading(heading)