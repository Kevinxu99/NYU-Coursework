n=int(input("Please enter a positive integer:"))
for i in range(1,n+1):
    print(" "*(n-i),sep="",end="")
    for j in range(1,i+1):
        print(j,sep="",end="")
    print("\n",end="")
    
