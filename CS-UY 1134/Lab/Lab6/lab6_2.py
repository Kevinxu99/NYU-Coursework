def total_sum(lst):
    temp_sum=0
    for curr in lst:
        if not isinstance(curr,int):
            temp_sum+=total_sum(curr)
        else:
            temp_sum+=curr
    return temp_sum
