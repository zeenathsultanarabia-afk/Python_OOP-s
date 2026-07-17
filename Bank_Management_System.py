class Customer:
  def __init__(self,name,account_number,pin):
    self.name= name
    self.account_number= account_number
    self.pin= pin
    self.balance= 0
    self.history= []

  def deposit(self,amount):

    if amount<=0:
      print("Invalid amount.")
      return
    self.balance+=amount
    self.history.append(f"Deposited ${amount}")
    print(f"Deposited Successfully")

  def withdraw(self,amount):
    if amount<=0:
      print("Invalid amount.")
      return
    if amount>self.balance:
      print("Insufficient funds.")
      return
    self.balance-=amount
    self.history.append(f"Withdrawn ${amount}")
    print(f"withdrawn Successfully")

  def check_balance(self):
    print(f"Available Balance: ${self.balance}")

  def show_history(self):
    if not self.history:
      print("No Transactions Found.")
      return
    print("\nTransaction History")
    for transaction in self.history:
      print(transaction)

class Bank:

  def __init__(self):
    self.customers= {}

  def create_account(self):
    print("\n---Create Account---")
    account_number= int(input("Enter Account Number: "))
    if account_number in self.customers:
      print("Account already exists")
      return
    name= (input("Enter Name: "))
    pin = input("Create 4-digit PIN:")

    customer = Customer(name,account_number,pin)
    self.customers[account_number]= customer
    print("Account Created Successfully.")

  def login(self):
      print("\n---Login---")
      account_number= int(input("Enter Account Number: "))
      pin = input("Enter PIN:")

      if account_number in self.customers:
        customer = self.customers[account_number]
        if customer.pin == pin:
            print(f"\nWelcome {customer.name}")
            return customer
            print("Invalid Account Number or PIN.")
            return None

bank = Bank()
while True:
  print("\n=======BANK MANAGEMENT SYSTEM======")
  print("1. Create Account")
  print("2. Login")
  print("3. Exit")

  choice = input("Enter your choice: ")

  if choice == "1":
    bank.create_account()
  
  elif choice == "2":
    customer = bank.login()
    if customer:
      while True:
        print("\n---------CUSTOMER MENU--------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Logout")
        option = input("Enter your choice: ")
        if option =="1":
          amount = float(input("Enter Amount: "))
          customer.deposit(amount)
        elif option=="2":
          amount= float(input("Enter Amount: "))
          customer.withdraw(amount)
        elif option=="3":
          customer.check_balance()
        elif option=="4":
          customer.show_history()
        elif option=="5":
          print("Logged Out Successfully.")
          break
        else:
          print("Invalid Choice.")
    elif choice == "3":
      print("Thank You.")
      break
    else:
      print("Invalid Choice.")
        


        

  
