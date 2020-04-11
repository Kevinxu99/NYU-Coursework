def sumSquare (lst):
    s=0
    for i in range (len(lst)):
        s+=(lst[i])**2
    return s

def main():
    lst=[1,2,3,4,5]
    print(sumSquare(lst))

main()
