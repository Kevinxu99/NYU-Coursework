n=int(input("Please enter a positive integer:"))
for i in range(1,n+1):
    odd=0
    even=0
    j=i
    while(j>0):
        if((j%10)%2==0):
            even+=1
        else:
            odd+=1
        j=j//10
    if(even>odd):
        print(i)
    
