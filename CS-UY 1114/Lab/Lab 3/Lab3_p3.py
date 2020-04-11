a=float(input("Please enter the first leg: "))
b=float(input("Please enter the second leg: "))
c=float(input("Please enter the hypotenuse: "))
if (((a*a+b*b)*1000)-5<=((c*c)*1000) and ((a*a+b*b)*1000)+5>=((c*c)*1000)):
    print(a,",",b,"and",c,"form a right triangle")
else:
    print(a,",",b,"and",c,"can't form a right triangle")

            
