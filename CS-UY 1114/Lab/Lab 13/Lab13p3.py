import random
def generate_number(lst):
    while(1):
        n=random.randint(10000,99999)
        t=0
        for i in lst:
            if i.library_account_number==n:
                t=1
        if t==0:
            return n
        
class Patron:
    def __init__(self,name):
        self.name=name
        self.library_account_number='None'
        self.booklst=[]

class Library:
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self.patrons=[]
        self.avabooks=[]

    def add_patron(self,patron):
        self.patrons.append(patron)
        patron.library_account_number=generate_number(self.patrons)

    def add_book(self,bookname):
        self.avabooks.append(bookname)

    def lend(self,patron,bookname):
        if bookname in self.avabooks:
            self.avabooks.remove(bookname)
            patron.booklst.append(bookname)
        else:
            print(bookname,"is not available")

    def __repr__(self):
        lst="Namr: "+self.name+"\n"+"Location: "+self.location+"\n"+"\n"
        lst+="Available Books: \n"
        for i in self.avabooks:
            lst=lst+i+"\n"
        lst+='\n'
        lst+='Library Patron Information:\n'
        for i in self.patrons:
            lst=lst+"Name: "+i.name+'\n'+'Library Account Number: '+str(i.library_account_number)+'\n'+'\n'
            lst=lst+'Borrowed Books:\n'
            for j in i.booklst:
                lst=lst+j+'\n'
            lst=lst+'\n'
        return lst
    
def main():
    bk_library=Library("Brooklyn Public Library","6 Metrotech Center")
    bk_library.add_book("Ender's Game")
    bk_library.add_book("Ender's Shadow")
    bk_library.add_book("Shadow of the Hegemon")
    bob=Patron('Bob')
    print(bob.library_account_number)
    bk_library.add_patron(bob)
    print(bob.library_account_number)
    bk_library.lend(bob,"Ender's Game")
    print(repr(bk_library))

main()
            
