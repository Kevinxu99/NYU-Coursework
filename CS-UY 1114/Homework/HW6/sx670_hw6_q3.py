def first_word (phrase):
    p=phrase.find(" ")
    return phrase[:p]

def delete_first_word (phrase):
    p=phrase.find(" ")
    return phrase[p+1:]

def reverse_phrase (phrase):
    s=""
    while(phrase.find(" ")!=-1):
        s=first_word(phrase)+s
        phrase=delete_first_word(phrase)
        s=" "+s
    s=phrase+s
    return s

def main():
    phrase=input("Enter the phrase: ")
    print(reverse_phrase (phrase))

main()
