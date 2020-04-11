n=int(input("Please input a positive integer:"))
for i in range(n,0,-1):
    print(" "*(n-i),"*"*(2*i-1),sep="")
for i in range(1,n+1):
    print(" "*(n-i),"*"*(2*i-1),sep="")
