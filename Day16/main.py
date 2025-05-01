# from turtle import Turtle , Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("cyan")
# timmy.forward(100)


# my_creen = Screen()
# print(my_creen.canvheight)
# my_creen.exitonclick()

from prettytable import PrettyTable , TableStyle

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Eletric","Water","Fire"])

table.align = "l"
print(table)