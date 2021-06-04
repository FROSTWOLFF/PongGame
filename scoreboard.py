from turtle import Turtle

ALIGNMENT = "CENTER"
FONT = ("Arial", 40, "normal")


class Scoreboard(Turtle):
    def __init__(self, side):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.side = side
        self.goto(-100, 240)
        self.update_scoreboard()

    def update_scoreboard(self):
        if self.side == "left":
            self.goto(-100, 240)
        elif self.side == "right":
            self.goto(100, 240)
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
