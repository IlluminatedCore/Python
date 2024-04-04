from bank_accounts import *

Dave = BankAccount(1000, 'Dave')
Sara = BankAccount(2000, 'Sara')

# Dave.getbalance()
# Sara.getbalance()
print (" ")
#Dave.deposit(1000)

#Dave.withdraw(100)

Sara.transfer(100, Dave)

