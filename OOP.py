class BankAccount: #Parent Class
    def __init__(self, my_account_number, my_balance):
        self.account_number = my_account_number
        self.balance = my_balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        deposited_balance = self.balance + amount
        return deposited_balance
        
    def withdraw(self, amount):
        withdrawed_balance = self.balance - amount
        return withdrawed_balance
    

class SavingsAccount(BankAccount): #Child Class

    def __init__(self, my_account_number , my_balance, interest_rate):
        super().__init__(my_account_number , my_balance)
        self.interest_rate = interest_rate

    def interest_deposit(self,interset_rate):
        self.balance += self.interest_rate
        return self.balance
        
class CheckingAccount(BankAccount): #Child Class

    def __init__(self, my_account_number , my_balance, overdrawt_fee):
        super().__init__(my_account_number , my_balance)
        self.overdraft_fee = overdrawt_fee

    def fee_deposit(self,overdraft_fee):
        self.balance -= self.overdraft_fee
        return self.balance

    
account = BankAccount("102510", 1000)
print(account.withdraw(500))
print(account.get_balance())
print(account.deposit(400))
print(account.get_balance())