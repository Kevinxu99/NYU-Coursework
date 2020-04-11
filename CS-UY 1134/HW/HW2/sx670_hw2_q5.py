def split_parity(lst):
    i=0
    n=0
    while(n<=len(lst)):
        if(lst[i]%2==0):
            lst.append(lst.pop(i))
        else:
            i+=1
        n+=1


