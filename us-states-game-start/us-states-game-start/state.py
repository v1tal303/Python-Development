from turtle import Turtle

class State(Turtle):
    def __init__(self, x_cor, y_cor, state_input):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x_cor, y_cor)
        self.color("black")
        self.write(state_input, True, align="center")

