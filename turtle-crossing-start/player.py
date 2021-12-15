from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -290)
        self.setheading(90)
        self.shape("turtle")
        self.shapesize(stretch_len=1, stretch_wid=1)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def reset(self):
        self.goto(0, -290)

