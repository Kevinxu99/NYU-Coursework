def intersect(lst1,lst2):
    lst=[]
    i1=0
    i2=0
    while(i1<len(lst1) and i2<len(lst2)):
        if(lst1[i1]>lst2[i2]):
            i2+=1
        elif(lst1[i1]<lst2[i2]):
            i1+=1
        else:
            lst.append(lst1[i1])
            i1+=1
            i2+=1
    return lst

print(intersect([1,6,14,15],[2,6,14,19]))
