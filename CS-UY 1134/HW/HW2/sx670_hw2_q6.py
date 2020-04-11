def two_sum(srt_lst,target):
    i=0
    j=len(srt_lst)-1
    while(i<j):
        if(srt_lst[i]+srt_lst[j]>target):
            j-=1
        elif(srt_lst[i]+srt_lst[j]<target):
            i+=1
        else:
            return (i,j)
    return None

