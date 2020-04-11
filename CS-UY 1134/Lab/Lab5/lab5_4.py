def binary_search(srt_lst,val,low,high):
    if(high==low):
        if(val==low):
            return low
        else:
            return None
    mid=(low+high)//2
    if(val>srt_lst[mid]):
        return binary_search(srt_lst,val,mid+1,high)
    elif(val<srt_lst[mid]):
        return binary_search(srt_lst,val,low,mid)
    else:
        return mid
