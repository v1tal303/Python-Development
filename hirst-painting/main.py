# import colorgram

# colors = colorgram.extract('download.jpg', 30)
#
# first_color = colors[0]
# rgb = first_color.rgb
# hsl = first_color.hsl
# proportion = first_color.proportion
#
#
# list_of_colors = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     list_of_colors.append(new_color)
#
# print(list_of_colors)

from turtle import Turtle, Screen
import random


color_list = [(237, 224, 80), (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218), (204, 75, 12), (219, 161, 103), (234, 224, 4), (11, 23, 63), (29, 189, 111), (22, 107, 174), (16, 28, 177), (216, 134, 179), (8, 186, 216), (229, 167, 200), (210, 25, 148), (122, 190, 160), (7, 49, 26), (34, 136, 72), (63, 20, 7), (126, 219, 234), (190, 14, 4), (109, 87, 215), (140, 217, 202), (238, 64, 34), (71, 10, 28)]

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

for i in range(10):
    tim.sety((i * 50)-250)
    tim.setx(-250)
    for i in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)







screen.exitonclick()