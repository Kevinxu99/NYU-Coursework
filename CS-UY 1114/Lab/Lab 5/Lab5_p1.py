n=int(input("Please enter a number:"))
s=0
for i in range (1,n+1):
    for j in range (1,i+1):
        print(j,end="",sep="")
    print("\n",end="")
