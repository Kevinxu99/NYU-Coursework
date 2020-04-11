def f2():
    sa=input("Please enter the first string:")
    sb=input("Please enter the second string:")
    l=len(sa)
    f=1
    for i in range(0,l):
        if(sb.find(sa[i])!=-1):
            t=sb.find(sa[i])
            sb=sb[:t]+sb[t+1:]
        else:
            f=0
            break
    if(f==0):
        print("Flase")
    else:
        print("True")
f2()
            
