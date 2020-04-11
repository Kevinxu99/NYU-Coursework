a=int(input("Please enter a positive integer as the dividend:"))
b=int(input("Please enter a positive integer as the divisor:"))
q=-1
a1=a
while(a>0):
    q+=1
    a-=b
print("Quotient of",a1,"divided by",b,"is",q)
