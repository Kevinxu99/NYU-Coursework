def find_duplicates(lst):
    cnt=[0 for i in range(len(lst))]
    for val in lst:
        cnt[val]+=1
    dup_lst=[]
    for i in range(1,len(lst)):
        if cnt[i]>1:
            dup_lst.append(i)
    return dup_lst
