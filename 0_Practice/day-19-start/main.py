from turtle import Turtle, Screen
import random


screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = list()

is_race_on = False

for i in colors:
    turtles.append(Turtle(shape="turtle"))
    turtles[colors.index(i)].penup()
    turtles[colors.index(i)].color(i)
    turtles[colors.index(i)].goto(-230, colors.index(i)*30-100)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost. The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()