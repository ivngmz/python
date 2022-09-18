class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())
    
    def withdraw(self, amount):
        self.balance =self.balance - amount

    def deposit(self, amount):
        self.balance =self.balance + amount
    
    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

# Herencia
class Checking(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee
    
checking=Checking("account//balance.txt", 52)
checking.deposit(10)

# account=Account("account//balance.txt", 1)
# print(account.balance) 
# account.withdraw(1)
# print(account.balance)
# checking.deposit(10000)
print(checking.balance)
checking.transfer(5000)
checking.commit()
print(checking.balance)