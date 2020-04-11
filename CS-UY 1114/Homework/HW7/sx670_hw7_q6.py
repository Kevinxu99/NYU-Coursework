def reverse_to_new_list(lst):
    lst1=[]
    for i in range(len(lst)):
        lst1.append(lst[len(lst)-1-i])
    return lst1

def reverse_in_place(lst):
    for i in range(len(lst)):
        lst.insert(len(lst)-1-i,lst.pop(0))
    return lst
    
def main():
    lst1 = [1, 2, 3, 4, 5, 6]
    rev_lst1 = reverse_to_new_list(lst1)
    print("After reverse_to_new_list, lst1 is", lst1,"and the returned list is", rev_lst1)
    lst2 = [1, 2, 3, 4, 5, 6]
    print("Before reverse_in_place, lst2 is", lst2)
    reverse_in_place (lst2)
    print("After reverse_in_place, lst2 is", lst2)

main()
