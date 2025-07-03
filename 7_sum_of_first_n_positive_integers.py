"""
Exercise 7: Sum of the First n Positive Integers
(Solved—12 Lines)
Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
sum = (n)(n + 1)/2
"""

n = int(input("Please enter a positive integer n. "))
sum_to_n = int((n)*(n+1)/2)
print(f"The sum of all positive integers from 1 to {n} is {sum_to_n}")
