def f4():
    n=int(input("Please enter a number:"))
    a=0
    while(2**a<n):
        a+=1
    a1=a-1
    n1=n
    s=""
    for i in range(0,a):
        if(2**a1<=n1):
            s+='1'
            n1=n1-(2**a1)
        else:
            s+='0'
        a1-=1
    ans=0
    for i in range (len(s)-1,-1,-1):
        if(s[i]=='0'):
            ans=ans+(2**i)
    if(n==0):
        print("1")
    else:
        print(ans)

f4()
    
