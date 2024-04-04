class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_amnt, acctname):
        self.balance = initial_amnt
        self.name = acctname

        print(f"Account {self.name} created. Balance amount $ {self.balance:.2f}")
    
    def getbalance(self):
        print(f"Account {self.name}. Balance amount $ {self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f} in to {self.name}'s account, total balance now is ${self.balance:.2f}")
    
    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
        
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print("Withdraw complete ✅")
            self.getbalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
    
    def transfer(self, amount, account):
        try:
            self.viable_transaction(amount)
            self.withdraw(amount)  
            account.deposit(amount)
            print('\nTransfer complete! ✅\n\n**********')
        except BalanceException as error:
            print(f'\Transfer incomplete: {error}')

