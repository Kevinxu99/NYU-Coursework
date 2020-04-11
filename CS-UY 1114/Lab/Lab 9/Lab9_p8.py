def circular_shift_list1(lst,k):
    k=k%len(lst)
    lst1=[]
    for i in range (len(lst)-k):
        lst1.append(lst[i])
    for i in range (k):
        lst1.insert(0,lst[len(lst)-1-i])
    return lst1

def main():
    lst=[1,2,3,4,5,6,7,8]
    k=int(input("Enter the number of steps: "))
    print(circular_shift_list1(lst,k))
    
main()
