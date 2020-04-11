
class ToDoList:
    def __init__(self):
        self.item=[]
        self.check=[]
    def create_to_do_list_item(tdl):
        self.item.append(input("Enter the task: "))
        self.check.append(0)
    def check_to_do_list(self):
        for i in range (0,len(self.item)):
            check=input("Did you "+self.item[i]+"?"+"(y/n) ")
            if(check=='y'):
                self.check[i]=1
        print("\nUpdated To-Do List:\n")
        print(repr(self))
    def __repr__(self):
        s="Today's Accomplishment\n"+"=========================\n"
        for i in range (0,len(self.item)):
            if(self.check[i]==1):
                s=s+self.item[i]+"\n"
        s=s+"\nThings Left To Do\n"+"=========================\n"
        for i in range (0,len(self.item)):
            if(self.check[i]==0):
                s=s+self.item[i]+"\n"
        return s

class Calendar:
    #to_do_list=ToDoList()
    def __init__ (self):
        s=input("Please enter today's date in mm/dd/yy format: ")
        w=input("Please enter the day of the week today (1 for Monday and 7 for Sunday): ")
        self.year=s[6:]
        self.month=s[:2]
        self.day=s[3:5]
        self.wn=w
        if(w=='1'):
            self.w='Monday'
        elif(w=='2'):
            self.w='Tuesday'
        elif(w=='3'):
            self.w='Wednesday'
        elif(w=='4'):
            self.w='Thursday'
        elif(w=='5'):
            self.w='Friday'
        elif(w=='6'):
            self.w='Saturday'
        elif(w=='7'):
            self.w='Sunday'
        self.to_do_list=ToDoList()
    def __repr__ (self):
        s="Today's date is: "+self.w+" "+self.month+"/"+self.day+"/"+self.year+"\n"
        s=s+"\n"+repr(self.to_do_list)
        return s
    def start_new_day (self):
        if (int(self.day)==31):
            if(int(self.month)==12):
                self.month='01'
                self.year=str(int(self.year)+1)
                if(len(self.year)==1):
                    self.year='0'+self.year
            else:
                self.month=str(int(self.month)+1)
                if(len(self.month)==1):
                    self.month='0'+self.month
            self.day='01'
        elif (int(self.day)==30):
            if(int(self.month)==4 or int(self.month)==6 or int(self.month)==9 or int(self.month)==11):
                self.month=str(int(self.month)+1)
                if(len(self.month)==1):
                    self.month='0'+self.month
                self.day='01'
        elif (int(self.day)==28 and int(self.month)==2):
            self.month='03'
            self.day='01'
        else:
            self.day=str(int(self.day)+1)
            if(len(self.day)==1):
                self.day='0'+self.day
        if(self.wn=='7'):
            self.wn='1'
        else:
            self.wn=str(int(self.wn)+1)
        if(self.wn=='1'):
            self.w='Monday'
        elif(self.wn=='2'):
            self.w='Tuesday'
        elif(self.wn=='3'):
            self.w='Wednesday'
        elif(self.wn=='4'):
            self.w='Thursday'
        elif(self.wn=='5'):
            self.w='Friday'
        elif(self.wn=='6'):
            self.w='Saturday'
        elif(self.wn=='7'):
            self.w='Sunday'
        self.to_do_list=ToDoList()
        print(repr(self))
 

def main():
    calendar=Calendar()
    while True:
        print("\nMain Menu:")
        print("1. Create New Calendar")
        print("2. Add To-Do List Item")
        print("3. Check Off To-Do List")
        print("4. Show Today's Calendar")
        print("5. Start The Next Day\n")
        answer=input("What would you like to do?")
        if answer == '1':
            calendar=Calendar()
        elif answer == '2':
            calendar.to_do_list.create_to_do_list_item()
        elif answer == '3':
            calendar.to_do_list.check_to_do_list()
        elif answer == '4':
            print(repr(calendar))
        elif answer == '5':
            calendar.start_new_day()

main()
