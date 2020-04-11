n=int(input("Please enter a positive integer:"))
d=int(input("Please enter the number of digits:"))
s=0
n1=n
while d>0:
    s+=n%10
    n=n//10
    d-=1
print("Sum of the last",d,"digits in",n1,"is:",s)
