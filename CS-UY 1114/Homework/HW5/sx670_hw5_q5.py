pw=input("Enter a password:")
up=0
low=0
di=0
sc=0
if(len(pw)<8):
    print(pw,"is not a valid password.")
else:
    for i in range (0,len(pw)):
        if(pw[i].isdigit()):
            di+=1
        elif(pw[i].isupper()):
            up+=1
        elif(pw[i].islower()):
            low+=1
        else:
            sc+=1
    if(up>=2 and low>=1 and di>=2 and sc>=1):
        print(pw,"is a valid password.")
    else:
        print(pw,"is not a valid password.")
