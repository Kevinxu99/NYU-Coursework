def print_oposite_triangle(n):
    if(n==0):
        return
    print("*"*n)
    print_oposite_triangle(n-1)
    print("*"*n)