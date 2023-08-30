class BankAccount():
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Balance.")

class SavingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)     ###/// ""super().__init__"" is used to call arguments/values from main/parent class.
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return float(self.balance*self.interest_rate/100)
    
    def totalbalance(self):
        return float(self.balance + (self.balance*self.interest_rate/100))
        
    
Account_1 = SavingAccount(123456, "John Wick", 2000, 10)
Account_1.deposit(1200)
Account_1.withdraw(600)
print("Balance: ", float(Account_1.balance))
Interest = Account_1.calculate_interest()
print(Interest)
Total_Balance = Account_1.balance + Interest
print("Total Balance: ", Total_Balance)