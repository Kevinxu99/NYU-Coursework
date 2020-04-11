jd=int(input("Please enter the number of days John has worked:"))
jh=int(input("Please enter the number of hours John has worked:"))
jm=int(input("Please enter the number of minutes John has worked:"))
bd=int(input("Please enter the number of days Bill has worked:"))
bh=int(input("Please enter the number of hours Bill has worked:"))
bm=int(input("Please enter the number of minutes Bill has worked:"))
tm=jm+bm+60*(jh+bh)+60*24*(jd+bd)
d=tm//(60*24)
h=(tm-d*(60*24))//60
m=tm%60
print("The total time both of them worked together is:",d,"days,",h,"hours and",m,"minutes.")
