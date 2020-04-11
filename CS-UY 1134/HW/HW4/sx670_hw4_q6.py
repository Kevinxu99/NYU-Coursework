def appearances(s,low,high):
    if(low>high):
        return {}
    ap=appearances(s,low+1,high)
    if(s[low] in ap):
        ap[s[low]]+=1
    else:
        ap[s[low]]=1
    return ap