r=int(input("Please enter an integer less than 100: "))
print(r,"in Roman Numeral is: ","L"*(r//50),"X"*((r%50)//10),"V"*((r%10)//5),"I"*(r%5))
