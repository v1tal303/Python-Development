from turtle import Turtle, Screen
import random
import colorgram

tim = Turtle()



tim.shape("turtle")
tim.color("red")
screen = Screen()
screen.colormode(255)
#
#
# # for i in range(20):
# #     tim.forward(10)
# #     tim.penup()
# #     tim.forward(10)
# #     tim.pendown()
#
#
#
#
# def draw_shape(sides):
#     angle = 360/sides
#     for i in range(sides):
#         tim.forward(100)
#         tim.left(angle)
#
#
#
# for i in range(3, 11):
#     draw_shape(i)


randomnumber = random.randint(1, 100)

print(randomnumber)



# def random_walk(seed):
#     if seed >= 66:
#         tim.left(90)
#         tim.forward(50)
#     elif seed >= 33:
#         tim.right(90)
#         tim.forward(50)
#     else:
#         tim.forward(50)
#
def random_color():
    R = random.randint(1, 255)
    G = random.randint(1, 255)
    B = random.randint(1, 255)
    tim.pencolor(R, G, B)
#
# tim.pensize(10)
#
# for i in range(10):
#     randomnumber = random.randint(1, 100)
#     random_color()
#     random_walk(randomnumber)

tim.speed("fastest")
for i in range(0, 360, 5):
    random_color()
    tim.setheading(i)
    tim.circle(100)



screen.exitonclick()