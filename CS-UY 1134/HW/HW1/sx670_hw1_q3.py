def Q3a(n):
    s=0
    for i in range(1,n):
        s+=(i*i)
    return s

#Q3b
s=sum([i*i for i in range(1,n)])
print (s)

def Q3c(n):
    s=0
    for i in range(1,n):
        if(i%2==1):
            s+=i*i

#Q3d
s=sum(i*i for i in range(1,n) if (i%2==1))
print s
