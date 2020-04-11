def add_entry(phonebook,name,phone_number):
    if(lookup(phonebook,name)=="Error"):
        if(len(phone_number)==10 and phone_number.isdigit()):
            phonebook[name]=phone_number
        else:
            print(phone_number,"is not a valid phone number")
    else:
        print(name,"already exist in the phone book")

def lookup(phonebook,name):
    if name in phonebook:
        return phonebook[name]
    else:
        return "Error"

def print_all(phonebook):
    for key in phonebook:
        print(key,": ",phonebook[key],sep="")

def main():
    f=open("Lab 13 - phonebook.txt","r")
    phonebook={}
    for line in f:
        lst=line.split(",")
        lst1=lst[1].split()
        name=lst1[0]+" "+lst[0]
        phone_number=lst1[1]
        add_entry(phonebook,name,phone_number)
    print_all(phonebook)
    f.close()
    
main()
