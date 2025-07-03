"""
Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies.
"""

def main():
    change = int(input(f"Please enter your change as an integer number of cents. "))
    change_output(change)

def change_output(change):
    # Create a dictionary to hold the denominations and their values
    denom_amounts = {"toonies": 200, "loonies": 100, "dimes": 10, "nickels": 5, "pennies": 1}
    # Initialize a breakdown dictionary to hold the count of each denomination
    # Initialize the breakdown dictionary with zero counts
    breakdown = {"toonies": 0, "loonies": 0, "dimes": 0, "nickels": 0, "pennies": 0}
    
    # Iterate through the denominations and calculate how many of each denomination is needed
    for key in denom_amounts.keys():
        breakdown[key] = change // denom_amounts[key]
        change = change % denom_amounts[key]
    print(breakdown)

# The following line is used to run the main function when the script is executed
main()

