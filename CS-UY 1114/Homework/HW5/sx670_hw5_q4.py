w=input("Enter a word:")
w1=w.lower()
count=0
for i in range(0,len(w1)):
    if(w1[i]=='a' or w1[i]=='e' or w1[i]=='o' or w1[i]=='u' or w1[i]=='i'):
        count+=1
print(w,"has",count,"vowels and",(len(w)-count),"consonants")
    
    
    
