
class BankAccount:
    def __init__(self,my_owner,my_balance = 0):
        self.owner = my_owner
        if my_balance >= 0:
            self.__balance = my_balance
        else:
            raise ValueError("Invalid deposint amount.")
        
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balamce(self,amount):
        
        
        def deposit
        if amount >= 0:
            self.__balance += amount
        else:
            raise ValueError("Invalid deposit amount.")

   
    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Invalid withdraw amount")

account = BankAccount(my_owner="Ann Johnson", my_balance = 5000)

print(account.my_balance)
account.deposit = 3000
print(account.deposit)
account.withdraw = 2000
print(account.withdraw)