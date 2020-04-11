def permutations(lst,low,high):
    if(low==high):
        return [[lst[high]]]
    sub_per=permutations(lst,low,high-1)
    per=[]
    for i in sub_per:
        for j in range(0,len(i)):
            per.append(i.copy())
            per[len(per)-1].insert(j,lst[high])
        per.append(i.copy())
        per[len(per)-1].append(lst[high])
    return per