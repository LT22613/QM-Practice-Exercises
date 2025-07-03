"""
Exercise 12: Distance Between Two Points on Earth
(27 Lines)
The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth's
surface. 
The distance between these points, following the surface of the Earth, in
kilometers is: distance = 6371.01 x arccos(sin(t1) x sin(t2) + cos(t1) x cos(t2) x cos(g1 - g2))
The value 6371.01 in the previous equation wasn't selected at random. It is
the average radius of the Earth in kilometers.
Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers.
"""
import math

# Convert degrees to radians
l1, l2 = map(float, input("Enter the latitude of two points (degrees): ").split())
l1, l2 = math.radians(l1), math.radians(l2)
g1, g2 = map(float, input("Enter the longitude of two points (degrees): ").split())
g1, g2 = math.radians(g1), math.radians(g2)

# Calculate the distance    
d = 6371.01 * math.acos(math.sin(l1) * math.sin(l2) + math.cos(l1) * math.cos(l2) * math.cos(g1-g2))

print(f"The distance between the two points is {d} kilometers.")