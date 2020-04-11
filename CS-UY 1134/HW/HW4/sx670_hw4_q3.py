def print_triangle(n):
    if(n==0):
        return
    print_triangle(n-1)
    print("*"*n)

def print_oposite_triangle(n):
    if(n==0):
        return
    print("*"*n)
    print_oposite_triangle(n-1)
    print("*"*n)

def print_ruler(n):
    if(n==1):
        print("-")
        return
    print_ruler(n-1)
    print("-"*n)
    print_ruler(n-1)
