print("Please enter lengths of a triangle's sides")
a=float(input("Length of the first side:"))
b=float(input("Length of the second side:"))
c=float(input("Length of the third side:"))
if(a==b and a==c):
    print(a,",",b,",",c,"form an equilateral triangle.")
elif(a==b or b==c or a==c):
    if((a*a+b*b-c*c)<=0.00001):
        print(a,",",b,",",c,"form an isosceles right triangle.")
    else:
        print(a,",",b,",",c,"form an isosceles triangle that is not a right triangle")
else:
    print(a,",",b,",",c,"form a triangle that is not an isosceles and not an equilateral.")
