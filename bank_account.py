# Parent Class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner 
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ₹{amount}. New Balance: ₹{self.balance}"
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ₹{amount}. Remaining Balance: ₹{self.balance}"
        else:
            return "Insufficient balance!"
        
    def display(self):
        return f"Owner: {self.owner}, Balance: ₹{self.balance}"
        
# Child Class
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate 

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest ₹{interest:.2f} added. New Balance: ₹{self.balance:.2f}"
    
# Polymorphism in action
def show_account_info(account):
    print(account.display())

# Testing
acc1 = BankAccount("Ekta", 1000)
print(acc1.deposit(500))
print(acc1.withdraw(200))
print(acc1.display())

acc2 = SavingsAccount("Ekta", 2000)
print(acc2.add_interest())
show_account_info(acc2)