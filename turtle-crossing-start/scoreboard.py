from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-190, 250)
        self.color("black")
        self.write(f"Level: {self.score}", True, align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", True, align="center", font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.goto(-190, 250)
        self.write(f"Score: {self.score}", True, align="center", font=FONT)


