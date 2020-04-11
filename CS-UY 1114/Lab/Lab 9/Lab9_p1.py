def func (myInt, n):
    myList=[]
    for i in range(n):
        myList.append(myInt+i)
    return myList

def main():
    myInt=int(input("Please enter an interger:"))
    n=int(input("Please enter a positive interger n:"))
    print (func(myInt,n))

main()
