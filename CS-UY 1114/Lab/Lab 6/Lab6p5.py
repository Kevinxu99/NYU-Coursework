s=input("Please enter a string s: ")
t=0
for i in range(1,len(s)-1):
    if(s[i]==s[0] and (len(s)%i)==0):
        t=1
        for j in range(i,len(s),i):
            if(s[0:i]!=s[j:(j+i)]):
                t=0
        if(t==1):
            l=i
            break
if(t==1):
    print("The substring",s[0:l],"repeated",len(s)//l,"times in",s)
else:
    print("There are no repeating substrings in",s)
