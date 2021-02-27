from turtle import Turtle, Screen

# POSITIONS = [(-280, -20), (-280, 0), (-280, 20)]
BAR_LENGTH = 4
BAR_POS = 560


class Bar(Turtle):
    def __init__(self, side):
        super().__init__()
        self.segments = []
        self.create_bar(side)

    def create_bar(self, side: str):
        positions = self.create_positions(side)

        for position in positions:
            self.add_segment(position)

    @staticmethod
    def create_positions(side: str) -> list:
        positions = []
        y = -20
        x = BAR_POS

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

    # def bar_move():
    #     pass
