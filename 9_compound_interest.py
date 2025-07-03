"""
Exercise 9: Compound Interest
(19 Lines)
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.
"""

deposit = float(input(f"Please enter the amount you wish to deposit. "))
"""
year_1 = round(deposit * (1.04),2)
year_2 = round(deposit * (1.04)**2,2)
year_3 = round(deposit * (1.04)**3,2)
print(f"After one year, the amount is: {year_1}")
print(f"After two years, the amount is: {year_2}")
print(f"After three years, the amount is {year_3}")
"""
list = []
for i in range(1,4):
    list.append(f"{deposit*(1.04)**i:.2f}")
for i in range(1,4):
    if i == 1:
        print(f"After 1 year, the amount is: {list[0]}")
    else:
        print(f"After {i} years, the amount is: {list[i-1]}")
     