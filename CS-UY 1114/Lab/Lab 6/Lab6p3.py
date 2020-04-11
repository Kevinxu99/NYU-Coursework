s=input("Please enter string s: ")
k=int(input("Please enter a number k: "))
print("The output is: ",sep="",end="")
t=1
for i in range(0,(len(s)//k)*k,k):
    if(t==1):
        for j in range(0,k):
            print(s[i+(k-j-1)],end="",sep="")
        t=0
    else:
        for j in range(0,k):
            print(s[i+j],end="",sep="")
        t=1
for i in range((len(s)-(len(s))%k),len(s)):
    print(s[i],end="",sep="")

