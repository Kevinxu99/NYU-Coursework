def f3():
    s=input("Please enter a string:")
    count=1
    for i in range (1,len(s)):
        if(s[i]!=s[i-1]):
            print(count,s[i-1],"'s")
            count=1
        else:
            count+=1
    print(count,s[len(s)-1],"'s")

f3()
