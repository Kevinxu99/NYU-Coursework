def sum_lst(lnk_lst):
    return sum_helper(lnk_lst,lnk_lst.header.next)

def sum_helper(lnk_lst,lnk_lst_node):
    if lnk_lst_node is not lnk_lst.trailer:
        sum=sum_helper(lnk_lst, lnk_lst_node.next)
        sum+=lnk_lst_node.data
    else:
        sum = 0
    return sum