"""
Exercise 10: Arithmetic
(Solved—20 Lines)
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
"""
import math

a = float(input("Please enter a number a. "))
b = float(input("Please enter a number b. "))
print(f"The sum of a and b is: {a+b}")
print(f"The difference between a and b is: {b-a}")
print(f"The product of a and b is: {a*b}")
print(f"The quotient when a is divided by b is {a / b}")
print(f"The remainder when a is divided by b is: {a % b}")
print(f"The result of log10a is: {math.log10(a)}")
print(f"The result of a^b is {a**b}")