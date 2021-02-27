from turtle import Turtle, Screen
from splitline import Splitline
from bars import Bar
import time

# Screen Properties
screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

split = Splitline()
split.draw_line()

left_bar = Bar("left")
right_bar = Bar("right")

game_on = True
while game_on:
    screen.update()

screen.mainloop()