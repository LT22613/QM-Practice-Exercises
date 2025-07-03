"""
Exercise 8:Widgets and Gizmos
(15 Lines)
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.
"""

widgets = int(input("Please enter the number of widgets you wish to order. "))
gizmos = int(input("Please enter the number of gizmos you wish to order. "))
print(f"The total weight of the order is {75*widgets+112*gizmos} grams. ")