def find_all(lst,val):
    lst_index=[]
    for i in range(len(lst)):
        if(val==lst[i]):
            lst_index.append(i)
    return lst_index

def main():
    lst=['a','b','10','aba','a']
    val='a'
    print(find_all(lst,val))

main()
