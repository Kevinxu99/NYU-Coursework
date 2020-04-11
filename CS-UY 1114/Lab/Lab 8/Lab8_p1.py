def f1():
    ch=input("Please enter a lowercase character:")
    n=int(input("Please enter a positivie integer:"))
    s=""
    for i in range(0,n):
        s=s+chr(((ord(ch)-ord('a')+i)%26)+ord('a'))
    print(s)


f1()
