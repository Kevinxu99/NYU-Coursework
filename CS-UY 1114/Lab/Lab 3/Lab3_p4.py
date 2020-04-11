a=int(input("Please enter a: "))
b=int(input("Please enter b: "))
if(a==0 and b==0):
    print("The equation has infinite number of solutions")
elif (a==0 and b!=0):
        print("The equation has no solution")
if (a!=0):
    print("The equation has single solution ans x=",(-b)/a)
