def print_shifted_triangle (n,m,symbol):
    for i in range (1,n+1):
        print(m*" ",(n-i)*" ",(2*i-1)*symbol,sep="")

def print_pine_tree (n,symbol):
    for i in range (2,n+2):
        print_shifted_triangle (i,n+1-i,symbol)

def main():
    n=int(input("Enter the number of triangles in the tree:"))
    symbol=input("Enter the character filling the tree:")
    print_pine_tree (n,symbol)

main()
