def sort_first(lst):
    pivot=lst[0]
    n=0
    i=0
    while(n<=len(lst)-1):
        if(lst[len(lst)-1]<pivot):
            lst.insert(0,lst.pop())
            i+=1
            n+=1
        else:
            lst.insert(i+1,lst.pop())
            n+=1