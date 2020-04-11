def list_min(lst,low,high):
    if(low==high):
        return lst[high]
    min_rest=list_min(lst,low+1,high)
    if(min_rest<lst[low]):
        return min_rest
    else:
        return lst[low]