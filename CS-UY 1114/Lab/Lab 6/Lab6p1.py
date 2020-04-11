s=input("Please enter a string:")
print("New string is: ",end="")
for i in range(0,len(s)):
    if(s[i]==" "):
        print(" ",sep="",end="")
    elif(s[i].isupper()):
        print(s[i].lower(),sep="",end="")
    elif(s[i].islower()):
        print(s[i].upper(),sep="",end="")
        
