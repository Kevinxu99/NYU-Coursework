import random
n=random.randrange(0,100)
print(n)
print("I thought of a number between 1 and 100!")
while(1):
    a=int(input("Try to guess what it is:"))
    if(a==n):
        print("Congrats! You guessed my number!")
        break
    elif (a>n):
        print("Wrong guess. My number is smaller than yours")
    else:
        print("Wrong guess. My number is bigger than yours")
