print("Please enter numbers of coins:")
q=int(input("# of quarters: "))
d=int(input("# of dimes: "))
n=int(input("# of nickels: "))
p=int(input("# of pennies: "))
c=q*25+d*10+n*5+p
print("The total is",c//100,"dollars and",c%100,"cents")
