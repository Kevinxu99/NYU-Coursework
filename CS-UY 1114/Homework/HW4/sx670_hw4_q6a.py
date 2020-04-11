import math
l=int(input("Please enter the length of the sequence:"))
p=1
for i in range(0,l):
    p*=int(input())
print("The geometric mean is:",p**(1./l))
