class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance

    def deposit(self,money):
        self.balance+=money
        
    def withdraw(self,money):
        if(money<=self.balance):
            self.balance-=money
        else:
            print("Insufficient balance. The current balance remained as $",str(self.balance),sep="")
            
    def __repr__(self):
        return "Current balance is: $"+str(self.balance)

def main():
    my_account=BankAccount('BOA123',1000)
    print(repr(my_account))
    my_account.deposit(100)
    print(repr(my_account))
    my_account.withdraw(500)
    print(repr(my_account))
    my_account.withdraw(999999)

main()
