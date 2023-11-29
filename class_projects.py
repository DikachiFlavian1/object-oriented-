"""this project is to  build a bank account class to try my level of understanding 
on classes, methods and functions
Bank Account Class:
Create a Python class called BankAccount that represents a simple bank account. 
It should have methods for deposit, withdrawal, and checking the account balance.
"""

class BankAccount:
 # i started first by creating a class and and initialize it with a constructor(__init__)   

    def __init__ (self,account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance
        
#2nd step is to add methods that performs basic bank features like withdraw,deposit and check balance

    def deposit (self,amount):
        self.balance += amount

    def withdraw (self,amount):
        if amount <= self.balance:
           self.balance -= amount
        else :
            print("insufficient fund") 

    def check_balance (self):
        """check current balance""" 
        return self.balance
    
#creating instances of BankAccount    
account1 = BankAccount("john") 
account2 = BankAccount("Bob",1000) 

#Deposit money into the accounts
account1.deposit(500)
account2.deposit(300)

# check the balances

print(f"{account1.account_holder}'s balance: ${account1.check_balance()}")
print(f"{account2.account_holder}'s balance: ${account2.check_balance()}")

#Withdraw money
account2.withdraw(500)




class BankAccount:
    def __init__(self):
        self.account_holder = input("Enter account holder's name: ")
        self.balance = 0

    def deposit(self, amount):
        """Add funds to the account."""
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        """Withdraw funds from the account, if sufficient balance is available."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        """Check the current balance of the account."""
        return self.balance

# Create an instance of BankAccount
account = BankAccount()

while True:
    print("\nOptions:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        amount = float(input("Enter the deposit amount: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter the withdrawal amount: "))
        account.withdraw(amount)
    elif choice == '3':
        print(f"Current balance: ${account.check_balance()}")
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
