text=input("Please enter a line of text:")
c=input("Please enter the character you want to remove:")
for i in range(0,len(text)):
    if(text[i]!=c):
        print(text[i],sep="",end="")
