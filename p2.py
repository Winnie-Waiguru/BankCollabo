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
        self.loan_balance=0
        

        
    def deposit(self,amount):
        if amount <=0:
            return f"Deposit amount should be more than zero"
        else:
            self.balance += amount
            self.deposits.append({"date":self.date.strftime('%c'), "amount":amount,"narration":"deposit"})
            return f"You deposited {amount}.Your new balance is {self.balance}"
             
    
    def withdraw(self, amount):
        if (amount+self.transaction)>self.balance:
            return f"Your balance is {self.balance}, you cannot withdraw the {amount}"
        elif amount<=0:
            return f"Amount must be greater than zero"
        else:    
            self.balance-=(amount +self.transaction)
            self.withdrawals.append({"date":self.date.strftime('%c'), "amount":amount,"narration":"Withdrawn"})
            return f"You withdrew {amount} and the transaction cost was {self.transaction}.Your new balane is {self.balance}"
        
