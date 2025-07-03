"""
Exercise 11: Fuel Efficiency
(13 Lines)
In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.
"""

US_efficiency = float(input("Please enter your efficiency in miles per gallon (MPG): "))
# Conversion factor from MPG to L/100 km
conversion_factor = 235.214583
Canada_efficiency = conversion_factor / US_efficiency
print(f"Your fuel efficiency in Canada is {Canada_efficiency:.2f} L/100 km.")
