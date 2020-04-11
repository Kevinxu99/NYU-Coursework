def square_root(num):
    i=1
    while(i*i<=num):
        i+=1
    if (i*i==num):
        return i
    n1=num*10000
    i=(i-1)*100
    for j in range(1,100):
        if((i+j)**2>n1):
            return (i+j-1)/100

print(square_root(874))
