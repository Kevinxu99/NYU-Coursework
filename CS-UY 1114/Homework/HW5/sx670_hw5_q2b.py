c=input("Enter a character:")
if(ord('a')<=ord(c) and ord(c)<=ord('z')):
    print(c,"is a lower case letter.")
elif(ord('A')<=ord(c) and ord(c)<=ord('Z')):
    print(c,"is an upper case letter.")
elif(ord('0')<=ord(c) and ord(c)<=ord('9')):
    print(c,"is a digit.")
else:
    print(c,"is a non-alphnumeric character.")
