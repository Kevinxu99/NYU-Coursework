def square_root(num):
    n=num*10000
    left=100
    right=n
    while(right-left>1):
        mid=(left+right)//2
        print(left," ",right)
        if(mid**2>n):
            right=mid
        elif(mid**2<n):
            left=mid
        elif(mid**2==n):
            return mid
    return (left/100)

print(square_root(1000))
