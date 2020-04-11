roman=input("Enter number in the simplified Roman system:\n")
s=0
for i in range (0,len(roman)):
    if(roman[i]=="M"):
        s+=1000
    if(roman[i]=="D"):
        s+=500
    if(roman[i]=="C"):
        s+=100
    if(roman[i]=="L"):
        s+=50
    if(roman[i]=="X"):
        s+=10
    if(roman[i]=="V"):
        s+=5
    if(roman[i]=="I"):
        s+=1
print(roman,"is",s)
