def count_lowercase(s,low,high):
    if(low>high):
        return 0
    rest_lc=count_lowercase(s,low+1,high)
    if(ord(s[low])>=ord('a') and ord(s[low])<=ord('z')):
        return 1+rest_lc
    else:
        return rest_lc