from turtle import Turtle, Screen


class Splitline(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pensize(4)
        self.penup()
        self.setpos(0, -300)
        self.hideturtle()
        self.setheading(90)
        self.speed("fastest")

    def draw_line(self):
        forward_counter = 1
        for _ in range(30):
            forward_counter += 1
            if forward_counter % 2 == 0:
                self.penup()
            else:
                self.pendown()
            self.forward(20)
