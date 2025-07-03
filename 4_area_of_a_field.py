"""
Exercise 4: Area of a Field
(Solved—15 Lines)
Create a program that reads the length and width of a farmer's field from the user in
feet. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre.
"""

length = float(input((f"Please enter the length of the field in feet. ") ))
width = float(input((f"Please enter the width of the field in feet. ")))
area_in_feet = length * width
area_in_acres = area_in_feet / 43560
# Round the area in acres to 4 d.p.
area_in_acres = round(area_in_acres, 4)
print(f"The area of the field is {area_in_acres} acres. ")


