"""
Exercise 14: Height Units

Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
Hint: One foot is 12 inches. One inch is 2.54 centimeters.
"""

print("Please enter your height in feet and inches. ")
feet = int(input("Feet: "))
inches = int(input("Inches: "))
cm_amount = 2.54 * (12*feet + inches)
print(f"Your height in cm is: {cm_amount}")


