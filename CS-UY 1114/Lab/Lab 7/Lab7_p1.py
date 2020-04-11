import random
n=int(input("Enter a number n:"))
for i in range(n,0,-1):
    for j in range(0,i):
        print(random.randrange(10),end="")
    print("")
for i in range(1,n+1,1):
    for j in range(0,i):
        print(random.randrange(10),end="")
    print("")
