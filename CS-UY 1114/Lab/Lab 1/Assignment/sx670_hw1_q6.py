print("Please enter your amount in the format of dollars and cents in two separate lines:")
dollar=int(input())
cent=int(input())
c=dollar*100+cent
q=c//25
d=(c%25)//10
n=(c-q*25-d*10)//5
p=c%5
print(dollar,"dollars and",cent,"cents are:")
print(q,"quarters,",d,"dimes,",n,"nickels,",p,"pennies")
