import random
def create_permutation(n):
    lst=[]
    for i in range (0,n):
        a=random.randint(0,n-1)
        while a in lst:
            a=random.randint(0,n-1)
        lst.append(a)
    return lst

def scramble_word(word):
    lst=create_permutation(len(word))
    sw=""
    for i in range(0,len(word)):
        sw=sw+word[lst[i]]
    return sw

def main():
    f=open("hw8 - word bank.txt","r")
    n=random.randint(1,101)
    for i in range (n):
       word=f.readline()
    word=word[:len(word)-1]
    nw=scramble_word(word)
    print("Unscramble the word: ",end="")
    for letter in nw:
        print(letter+" ",end="")
    print("\n")
    ans=input("Try #1: ")
    if ans == word:
        print("Yay you got it!")
    else:
        print("Wrong!")
        ans=input("Try #2: ")
        if ans == word:
            print("Yay you got it!")
        else:
            print("Wrong!")
            ans=input("Try #3: ")
            if ans == word:
                print("Yay you got it!")
            else:
                print("Wrong!")
    
main()
