from turtle import Turtle

COLOR = "white"
SHAPE = "square"


class paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(COLOR)
        self.shape(SHAPE)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
