# import turtle
#
# timmy = turtle.Turtle()
#
# print(timmy.color())
#
# my_screen = turtle.Screen()
# timmy.shape("turtle")
# timmy.color("cyan2")
# timmy.forward(100)
#
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()


print(table)

table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)