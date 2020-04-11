print("Please enter a non-empty sequence of positive integers, each one in a separate line. End your sequence by typing done:")
p=1
l=0
while(1):
    a=input()
    if(a=='done'):
        break
    p*=int(a)
    l+=1
print("The geometric mean is:",p**(1./l))
