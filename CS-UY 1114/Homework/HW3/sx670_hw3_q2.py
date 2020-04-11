pa=float(input("Enter price of first item:"))
pb=float(input("Enter price of second item:"))
cc=input("Does customer Have a club card? (Y/N):")
tax=float(input("Enter tax rate, e.g. 5.5 for 5.5% tax:"))
bp=pa+pb
print("Base Price=",bp)
if(pa>pb):
    dp=pa+pb/2
else:
    dp=pb+pa/2
if(cc=='Y' or cc=='y'):
    dp=dp*0.9
print("Price after discounts=",dp)
tp=dp+dp*(tax/100)
print("Total Price=%.2f"%tp)

