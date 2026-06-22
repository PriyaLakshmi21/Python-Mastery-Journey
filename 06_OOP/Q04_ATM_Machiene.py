class Transaction:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print("withdrawn:",amount)
            print("Remaining Balance:",self.balance)
        else:
            print("Insufficient Balance")
tans=Transaction("Priya",50000)
tans.withdraw(1000)
        