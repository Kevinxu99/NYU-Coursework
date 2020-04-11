s=input("Please enter a string of lowercase letters:")
t=1
for i in range(1,len(s)):
    if(ord(s[i])<=ord(s[i-1])):
        t=0
if(t==1):
    print(s,"is increasing.")
else:
    print(s,"is not increasing.")
