def remove_all(lst, value):
    n=0
    for i in range(len(lst)):
        if(lst[i]==value):
            n+=1
        else:
            lst[i-n]=lst[i]
    for i in range(n):
        lst.pop()
