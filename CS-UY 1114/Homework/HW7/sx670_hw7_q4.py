def create_prefix_lists(lst):
    prefixLst=[]
    bigLst=[]
    for i in range(len(lst)+1):
        bigLst.append([])
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            bigLst[j+1].append(lst[i])
    return bigLst

def main():
    lst=[2,4,6,8,10]
    print(create_prefix_lists(lst))

main()
    
