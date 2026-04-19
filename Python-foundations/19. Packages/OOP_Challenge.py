class Account():
    
    def __init__(self,owner, balance=0):
        self.owner = owner
        self.balance = balance
   
    def deposit(self,amt):
        self.balance = self.balance + amt
        print(f"{amt}$ deposited now the current balance is {self.balance}")
    
    def withdraw(self,amt):
        if self.balance >=amt:
            self.balance = self.balance - amt
            print(f"{amt}$ withdrawn now the current balance is {self.balance}")
        else:
            print(f"You don't have enough funds in your A/c please deposit sufficient funds first\nYour current A/c balance is {self.balance}")

    def __str__(self):
        return (f"A/c owner: {self.owner} \nA/c balance: {self.balance}")

a1 = Account("Jose",400)
print(a1.owner)
print(a1.balance)


