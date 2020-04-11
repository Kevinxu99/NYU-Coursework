s=input("Please enter string s: ")
print("Result: ",sep="",end="")
n=0
s2=""
for i in range(0,len(s)):
    if(s[i]!=" "):
        s2+=s[i]
        n+=1
    else:
        for j in range(0,n):
            print(s2[n-j-1],sep="",end="")
        print(" ",end="",sep="")
        s2=""
        n=0
for i in range(0,n):
    print(s[len(s)-1-i],sep="",end="")
