a=input("Please enter the first number:")
b=int(input("Please enter the second number:"))
l=len(a)
a=int(a)
s=0
a1=a
b1=b
for i in range (0,l):
    if((a%10)!=(b%10)):
        s=s+1
    a=a//10
    b=b//10
print("The Hamming Distance between",a1,"and",b1,"is",s)
