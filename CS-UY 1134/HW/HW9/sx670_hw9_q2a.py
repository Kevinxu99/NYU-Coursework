def intersection_list(lst1, lst2):
    lst1.sort()
    lst2.sort()
    i1 = 0
    i2 = 0
    intsec = []
    while i1 < len(lst1) and i2 < len(lst2):
        if(lst1[i1] < lst2[i2]):
            i1 += 1
        elif(lst1[i1] > lst2[i2]):
            i2 += 1
        else:
            intsec.append(lst1[i1])
            i1 += 1
            i2 += 1
    return intsec
