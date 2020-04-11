def count(lst, item):
    s=0
    for i in range (len(lst)):
        if (item==lst[i]):
            s+=1
    return s

def main():
    lst=[0,32,'a','0','4',15,'q','0']
    item=input("Enter the item:")
    print(count(lst,item))

main()
    
