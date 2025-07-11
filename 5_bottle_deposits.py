"""
Exercise 5: Bottle Deposits
(Solved—15 Lines)
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places.
"""

def refund(container_list):
    container_l = 0
    container_l_sum = 0
    container_s = 0
    container_s_sum = 0
    for container in container_list:
        if container > 1:
            container_l += 1
            container_l_sum += 0.25
        else:
            container_s += 1
            container_s_sum += 0.10
    total = round(container_l_sum + container_s_sum, 2)
    print(f"Your refund is ${total}.")

refund([0.5,1,7])
        
    