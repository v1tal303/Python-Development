from paddle import Paddle
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My pong game")


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.inrease_speed()


    if ball.xcor() > 400:
        ball.refresh()
        scoreboard.l_point()


    if ball.xcor() < -400:
        ball.refresh()
        scoreboard.r_point()





screen.exitonclick()
