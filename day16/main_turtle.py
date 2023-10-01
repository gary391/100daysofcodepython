# import another_module
# from turtle import Turtle, Screen
#
# print(another_module.another_variable)
# timmy = Turtle()  # constructing the turtle object using the ()
# print(timmy) # object
#
# timmy.shape("turtle")
# timmy.color("red","green")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvwidth) # height of the conv
# my_screen.exitonclick()
#
from prettytable import PrettyTable
table = PrettyTable() # this the syntax for creating the table.
table.add_column("name", ["renu", "sonu", "monu", "tanu"])
table.add_column("rollnumber",["1", "2", "3", "4"])
# Left aligned table
table.align = 'l'
print(table)