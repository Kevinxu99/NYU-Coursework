c=input("Enter a character:")
if c.isdigit():
    print(c,"is a digit.")
elif c.islower():
    print(c,"is a lower case letter.")
elif c.isupper():
    print(c,"is an upper case letter.")
else:
    print(c,"is a non-alphnumeric character.")
    
