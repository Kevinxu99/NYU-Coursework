class Person:
    def __init__ (self):
        self.name=input("Please enter the name:")
        self.age=input("Please enter the age:")
        self.hobbies=[]
        
    def addHobby (self,newHobby):
        self.hobbies.append(newHobby)

    def deleteHobby (self,oldHobby):
        self.hobbies.remove(oldHobby)

    def birthday (self):
        print("Happy birthday, ",self.name,"!",sep="")

    def __repr__ (self):
        s="Name: "+self.name+"\n"+"Age: "+self.age+"\n"+"Hobbies:"+"\n"
        if(len(self.hobbies)==0):
            return s+"None\n"+"\n"
        else:
            for i in self.hobbies:
                s=s+i+"\n"
            return s+"\n"

def main():
    people=[]
    while(1):
        print("Select one of the following options:")
        print("="*40)
        print("1. Create a new Person")
        print("2. Add to an existing person's hobbies")
        print("3. Delete an existing person's hobby")
        print("4. Someone has a birthday")
        print("5. See a list of people")
        print("6. Exit")
        n=int(input())
        if(n==1):
            people.append(Person())
        if(n==2):
            name=input("Who is receiving a new hobby?")
            for i in people:
                if (i.name==name):
                    i.addHobby(input("What is this person's new hobby?\n"))
        if(n==3):
            name=input("Who is losing a hobby?")
            for i in people:
                if (i.name==name):
                    i.deleteHobby(input("What hobby are you deleting?"))
        if(n==4):
            name=input("Who is having a birthday?")
            for i in people:
                if (i.name==name):
                    i.birthday()
        if(n==5):
            for i in people:
                print(repr(i))
        if(n==6):
            print("Goodbye!")
            break
        print("\n")

main()       
