n=int(input("Please enter a date of birth: "))
m=int(input("Please enter today's date: "))
ny=n//10000
nm=(n%10000)//100
nd=n%100
my=m//10000
mm=(m%10000)//100
md=m%100
print("Date of birth is",nm,"/",nd,"/",ny)
print("Today's Date is",mm,"/",md,"/",my)
