def find_lst_max(lst):
    if(len(lst)==1):
        return lst[0]
    mid=(len(lst)-1)//2
    left=find_lst_max(lst[:mid+1])
    right=find_lst_max(lst[mid+1:])
    if(left>right):
        return left
    else:
        return right
