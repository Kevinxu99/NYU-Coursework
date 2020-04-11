n=int(input("Enter the number of sides: "))
if(n==3):
    print("The shape is triangle")
if(n==5):
    print("The shape is pentagon")
if(n==4):
    a=input("Are the sides equal? (Y/N): ")
    if(a=='Y'):
        print("The shape is square")
    else:
        b=input("Are the angles 90 degrees? (Y/N): ")
        if(b=='Y'):
            print("The shape is rectangle")
        else:
            print("The shape is quadrilateral")
    
