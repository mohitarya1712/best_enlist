class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Your Account is Created")
  
    def deposit(self):
        amount = float(input("\nEnter amount to be deposit:"))
        self.balance += amount
        print("Amount Deposited:",amount)
  
    def withdraw(self):
        amount = float(input("\nEnter amount to be withdraw:"))
        if self.balance >= amount:
            self.balance -= amount
            print("You Withdrew:", amount)
        else:
            print("Insufficient balance")
  
    def display(self):
        print("\nNet Available Balance = ",self.balance)
  
s = Bank_Account()
   
s.deposit()
s.withdraw()
s.display()
