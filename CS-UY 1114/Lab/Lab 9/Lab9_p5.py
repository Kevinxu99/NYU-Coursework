def get_common_element(lst1,lst2):
    lst=[]
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if(lst1[i]==lst2[j]):
                t=0
                for k in range (len(lst)):
                    if(lst1[i]==lst[k]):
                        t=1
                if(t==0):
                    lst.append(lst1[i])
    return lst

def main():
    lst1=[2,'S',2,2,2,2,2,2,2,2,3.13,3.13,'python']
    lst2=['pythy',2,12,'hello',2,2,2,2,2,2,3.13]
    print(get_common_element(lst1,lst2))

main()
