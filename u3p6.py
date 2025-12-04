import sys
class bank(object):
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def withdrawals(self,amount):
        if amount > self.balance:
            print("Low balance,Cannot Withdraw")
        else:
            self.balance -=amount
        return self.balance
name=input("Enter Name:")
balance = float(input("Enter an Initial Balance:"))
b = bank(name, balance)
while(True):
    print("d/D -Deposit,w/W -Withdrawls, e/E -Exit")
    choice=input("Enter Your Choice:")
    if choice=="e" or choice=="E":
            sys.exit()
    amount= float(input("Enter amount:"))
    if choice=="d"  or choice=="D":
        print("Balance After Deposite",b.deposit(amount))
    elif choice=="w" or  choice== "W":
            print("Balance After Withdrawal",b.withdrawals(amount))
            
