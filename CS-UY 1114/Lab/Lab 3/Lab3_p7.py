t=int(input("Please enter time in 24 hr format: "))
h=t//100
m=t%100
if(h<=12):
    if(h==0):
        print(t//1000,(t//100)%10,":",(t%100)//10,t%10,"in 12 hr format is: 12 :",(t%100)//10,t%10,"am")
    elif (h==12):
        print(t//1000,(t//100)%10,":",(t%100)//10,t%10,"in 12 hr format is: 12 :",(t%100)//10,t%10,"pm")
    else:
        print(t//1000,(t//100)%10,":",(t%100)//10,t%10,"in 12 hr format is:",t//1000,(t//100)%10,":",(t%100)//10,t%10,"am")
else:
    print(t//1000,(t//100)%10,":",(t%100)//10,(t%10),"in 12 hr format is",(h-12)//10,(h-12)%10,":",(t%100)//10,(t%10),"pm")
