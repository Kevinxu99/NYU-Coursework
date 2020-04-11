def remove_below_avg(lst):
    s=0
    for i in range(len(lst)):
        s+=lst[i]
    avg=s/len(lst)
    i=0
    while(i<len(lst)):
        if (lst[i]<avg):
            lst.remove(lst[i])
        else:
            i+=1
    return lst

def main():
    lst=[2,3,5,1,-4,8,0,-1]
    print(remove_below_avg(lst))

main()
