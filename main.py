from turtle import Turtle, Screen
from splitline import Splitline
from bars import Bar
from ball import Ball
import time

# Screen Properties
screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

# Created Classes
split = Splitline()
player1 = Bar("left")
player2 = Bar("right")
ball = Ball()

# Class functions being used
split.draw_line()

# Defining button listenings
screen.listen()
# Player 1
screen.onkeypress(player1.move_up, "w")
screen.onkeypress(player1.move_down, "s")
# Player 2
screen.onkeypress(player2.move_up, "Up")
screen.onkeypress(player2.move_down, "Down")

game_on = True
while game_on:
    screen.update()
    ball.forward(1.3)
    # Ball wall collision check
    if ball.ycor() > 280:
        ball.wall_col_top()
    elif ball.ycor() < -280:
        ball.wall_col_bot()
    # time.sleep(0.05)

screen.mainloop()