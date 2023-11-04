class Bank:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check(self):
        print(self.balance)
        
bank1 = Bank("Edric", 12345, 100)
bank1.check()
bank1.deposit(50)
print()
bank1.check()
bank1.withdraw(150)
print()
bank1.check()

