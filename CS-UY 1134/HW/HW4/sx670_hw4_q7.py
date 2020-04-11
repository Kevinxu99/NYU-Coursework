def split_by_sign(lst,low,high):
    if(low>high):
        return
    if(lst[low]>0):
        lst.append(lst.pop(low))
        split_by_sign(lst,low,high-1)
    else:
        split_by_sign(lst,low+1,high)