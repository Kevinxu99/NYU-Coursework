import random
n=random.randrange(1,100)
print("I thought of a number between 1 and 100! Try to guess it.\n")
r=100
l=1
for i in range(5,0,-1):
    print("Range:[",l,",",r,"], Number of guesses left:",i,sep="")
    a=int(input("Your guess:"))
    if(a==n):
        if(i==5):
            print("Congrats! You guessed my number in 1 guess")
        else:
            print("Congrats! You guessed my number in",n-i+1,"guesses",sep="")
        break
    elif(a>n and i!=1):
        print("Wrong! My number is smaller.\n")
        r=a-1
    elif(a<n and i!=1):
        print("Wrong! My number is bigger.\n")
        l=a+1
    else:
        print("Out of guesses! My number is",n)
        
