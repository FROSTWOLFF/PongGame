from turtle import Turtle, Screen
from splitline import Splitline
from bars import Bar
from ball import Ball
import time

BALL_SPEED = 1.3

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
    ball.forward(BALL_SPEED)
    # Ball Collisions
    # Bar collision check player1
    for seg in player1.segments:
        segment_pos = seg.position()
        if ball.distance(segment_pos) < 25:
            ball.bar_col_left()
            BALL_SPEED += 0.1
            print("collided")

    # Bar collision check player2
    for seg in player2.segments:
        segment_pos = seg.position()
        if ball.distance(segment_pos) < 25:
            ball.bar_col_right()
            BALL_SPEED += 0.1
            print("collided")

    # Wall collision check
    if ball.ycor() > 280:
        ball.wall_col_top()

    elif ball.ycor() < -280:
        ball.wall_col_bot()

    # time.sleep(0.01)

screen.mainloop()