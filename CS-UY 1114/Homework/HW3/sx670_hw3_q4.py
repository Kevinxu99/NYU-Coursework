a=float(input("Please enter value of a:"))
b=float(input("Please enter value of b:"))
c=float(input("Please enter value of c:"))
delta=b*b-4*a*c
if(a==0 and b==0 and c==0):
    print("This equation has infinite number of solutions")
elif(a==0 and b!=0):
    print("This equation has single real solution x=",(-c)/b)
elif(a==0 and b==0):
    print("This equation has no solution")
elif(delta<0):
    print("This equation has no solution")
elif(delta==0):
    print("This equation has single real solution x=",(-b)/(2*a))
else:
    print("This equation has two real solutions x1=",(-b+delta)/(2*a),"x2=",(-b-delta)/(2*a))
    
