# Encapsulation Example - Use private variables to hide internal data

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable (not accessible directly)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # Safely modify balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount  # Deduct amount safely
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance  # Access balance through method

# Create bank account object
acc = BankAccount("Arjun", 5000)
acc.deposit(2000)   # Deposit money
acc.withdraw(1000)  # Withdraw money

# Print balance using method
print("Balance:", acc.get_balance())

# print(acc.__balance)  # ❌ Error: Private variable, cannot access directly

'''
Output:
Balance: 6000
'''
