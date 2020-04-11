L=[2,3,5,6,8,8]
lst=[L[i] for i in range(len(L)-1) if (L[i]%2==0 and i%2==0)]
print(lst)
