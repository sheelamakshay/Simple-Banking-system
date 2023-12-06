class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            print(f"Account created successfully for {account_number} with initial balance: ${initial_balance}")
        else:
            print(f"Account already exists for {account_number}")

    def view_balance(self, account_number):
        if account_number in self.accounts:
            balance = self.accounts[account_number]
            print(f"Balance for account {account_number}: ${balance}")
        else:
            print(f"Account {account_number} not found")

    def deposit_money(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"${amount} deposited successfully into account {account_number}")
            self.view_balance(account_number)
        else:
            print(f"Account {account_number} not found")

    def withdraw_money(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print(f"${amount} withdrawn successfully from account {account_number}")
                self.view_balance(account_number)
            else:
                print("Insufficient funds")
        else:
            print(f"Account {account_number} not found")


# Example usage with user input:
bank = Bank()

while True:
    print("\n1. Create Account\n2. View Balance\n3. Deposit Money\n4. Withdraw Money\n5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        account_number = input("Enter account number: ")
        bank.create_account(account_number)
    elif choice == '2':
        account_number = input("Enter account number: ")
        bank.view_balance(account_number)
    elif choice == '3':
        account_number = input("Enter account number: ")
        amount = float(input("Enter the deposit amount: $"))
        bank.deposit_money(account_number, amount)
    elif choice == '4':
        account_number = input("Enter account number: ")
        amount = float(input("Enter the withdrawal amount: $"))
        bank.withdraw_money(account_number, amount)
    elif choice == '5':
        print("Exiting the banking system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
