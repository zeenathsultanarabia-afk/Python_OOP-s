class ATM:
     def __init__(self,account_holder,balance):
       self.account_holder = account_holder
       self.balance = balance

     def deposit(self,amount):
       self.balance+=amount
       return f"${amount} deposited successfully."

     def withdraw(self,amount):
        if amount<= self.balance:
         self.balance -=amount
         return f"${amount} withdrawn successfully."
        else:
         return f"Insufficient Balance."

     def check_balance(self):
        return f"Available Balance: ${self.balance}"

     def account_details(self):
       return f"Account Holder: {self.account_holder}\nCurrent Balance: ${self.balance}"






user1= ATM("Rahul",5000)

print(user1.account_details())
print(user1.deposit(2000))
print(user1.withdraw(1500))
print(user1.check_balance())
