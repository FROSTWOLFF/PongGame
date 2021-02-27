from turtle import Turtle, Screen
from splitline import Splitline
import time

# Screen Properties
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

split = Splitline()
split.draw_line()

game_on = True
while game_on:
    screen.update()

screen.mainloop()