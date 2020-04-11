def find_max_even_index(lst):
    max_even=0
    max_index=-1
    for i in range(len(lst)):
        if(lst[i]%2==0):
            if(lst[i]>max_even):
                max_even=lst[i]
                max_index=i
    return max_index

def main():
    lst=[56,24,58,10,33,95]
    print(find_max_even_index(lst))

main()
