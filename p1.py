from datetime import datetime


class Account:
    def __init__(self,account_name, account_number):
        self.balance=0
        self.account_name=account_name
        self.account_number=account_number
        self.deposits=[]
        self.withdrawals=[]
        self.transaction= 100
        self.date=datetime.now()
        
         

        
    def deposit(self,amount):
        if amount <=0:
            return f"Deposit amount should be more than zero"
        else:
            self.balance += amount
            self.deposits.append({"date":self.date, "amount":amount,"narration":"deposit"})
            return f"You deposited {amount}.Your new balance is {self.balance}"
             
    
