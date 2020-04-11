def add_list(lst1,lst2):
    lst=[]
    for i in range(len(lst1)):
        lst.append(lst1[i]+lst2[i])
    return lst

def main():
    lst1=[]
    lst2=[]
    while(1):
        a=input()
        if(a!='done'):
            lst1.append(int(a))
        else:
            break
    while(1):
        a=input()
        if(a!='done'):
            lst2.append(int(a))
        else:
            break
    if(len(lst1)!=len(lst2)):
        print("Lists are different lengths")
    else:
        print(add_list(lst1,lst2))

main()
