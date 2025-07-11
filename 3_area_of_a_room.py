"""
Exercise 3: Area of a Room
(Solved—13 Lines)
Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.
"""

length = float(input((f"Please enter the length of the room in metres. ") ))
width = float(input((f"Please enter the width of the room in metres. ")))
area = length * width
print(f"The area of the room is {area} metres squared.")