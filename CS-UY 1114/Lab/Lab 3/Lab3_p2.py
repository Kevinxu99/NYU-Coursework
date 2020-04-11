name=input("Please enter your name:")
gy=int(input("Please enter your graduation year:"))
cy=int(input("Please enter current year:"))
a=gy-cy
if (a>4):
    print(name,"is not in college yet")
if (a==4):
    print(name,"is a freshman")
if (a==3):
    print(name,"is a sophomore")
if (a==2):
    print(name,"is a junior")
if (a==1):
    print(name,"is a senior")
if (a<=0):
    print(name,"is graduated")
        
