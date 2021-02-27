from turtle import Turtle, Screen

# POSITIONS = [(-280, -20), (-280, 0), (-280, 20)]
BAR_LENGTH = 4
BAR_POS = 560
BAR_SPEED = 42


class Bar(Turtle):
    def __init__(self, side):
        super().__init__()
        self.segments = []
        self.create_bar(side)

    # Creating a bar section
    def create_bar(self, side: str):
        positions = self.create_positions(side)

        for position in positions:
            self.add_segment(position)

    @staticmethod
    def create_positions(side: str) -> list:
        positions = []
        x = BAR_POS
        y = -20

        if side == "left":
            x = -x

        for _ in range(BAR_LENGTH):
            new_position = (x, y)
            positions.append(new_position)
            y += 20

        return positions

    def add_segment(self, position: tuple):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(position)
        new_segment.speed("fastest")

        self.segments.append(new_segment)

    # Moving the bar
    def move_up(self):
        for seg in self.segments:
            seg.setheading(90)
            seg.forward(BAR_SPEED)

    def move_down(self):
        for seg in self.segments:
            seg.setheading(270)
            seg.forward(BAR_SPEED)
