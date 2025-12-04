class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct the amount from balance if sufficient funds are available."""
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew: ${amount}")
            return True
        else:
            print("Insufficient funds!")
            return False

    def display_balance(self):
        """Display the current account balance."""

        print(f"Current balance: ${self.__account_balance}")
        print(f"Current Balance: {self.__account_balance}")
