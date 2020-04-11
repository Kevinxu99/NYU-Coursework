n=int(input("Please enter a number:"))
for i in range (1,n+1):
    print("."*(n-i),end="",sep="")
    for j in range (0,i):
        print(i,end="",sep="")
    print("\n",end="")
