
class BankAccount:
    def __init__(self, my_account_holder, my_balance = 0):
        self.holder = my_account_holder
        self.balance = my_balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
        else:
            raise ValueError
        return self.balance
        
    def withdraw(self, amount):
        if amount >= 0:
            self.balance -= amount
        else:
            raise ValueError
        return self.balance
    
account = BankAccount("Bob White", 1000)
print(account.get_balance())
print(account.deposit(500))
print(account.withdraw(300))
print(account.get_balance())