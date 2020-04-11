def max_abs_val(lst):
    max_val=0
    for i in range(len(lst)):
        if(abs(lst[i])>max_val):
            max_val=lst[i]
    return max_val

def main():
    lst=[-19,-3,20,-1,0,-25]
    print(max_abs_val(lst))

main()
