exp=input("Enter a mathmatical expression:")
i=0
while (exp[i]!=" "):
    i+=1
op=exp[i+1]
oprand1=int(exp[0:i])
oprand2=int(exp[i+3:len(exp)])
if(op=="+"):
    print(exp,"=",oprand1+oprand2)
if(op=="-"):
    print(exp,"=",oprand1-oprand2)
if(op=="*"):
    print(exp,"=",oprand1*oprand2)
if(op=="/"):
    print(exp,"=",oprand1/oprand2)
