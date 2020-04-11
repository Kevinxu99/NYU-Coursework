def product_evens(lst):
    if(lst[0]==-1):
        return 1
    if(lst[0]%2==0 and lst[0]<=len(lst)):
        return lst[0]*product_evens(lst[1:]+[-1])
    else:
        return product_evens(lst[1:]+[-1])