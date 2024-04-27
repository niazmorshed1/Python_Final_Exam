from random import randint

class AsiaBank:
    bank_balance = 500000
    bank_loan_amount = 0
    bank_loan_possible = True
    bank_user = []
    bankrupt = False

class User(AsiaBank):
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = randint(100, 999)
        self.transaction_history = []
        self.loan_taken = 0
        self.transfer_limit = 2 if self.account_type == 'Savings' else float('inf')
        
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self.account_type == 'Savings' and len(self.transaction_history) >= 3:
            print("Withdrawal limit exceeded")
            return
        if amount > self.balance:
            print("Withdrawal amount exceeds the current balance")
        elif amount <= 0:
            print("Invalid withdrawal amount")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            print("Withdrawal completed successfully")

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.loan_taken < 2:
            self.loan_taken += 1
            self.balance += amount
            self.transaction_history.append(f"Loan Taken: {amount}")
        else:
            print("Maximum number of loans already taken")

    def transfer(self, amount, other_account):
        if self.account_type == 'Savings' and len(self.transaction_history) >= 3:
            print("Transfer limit exceeded")
            return
        if amount > self.balance:
            print("Insufficient balance to transfer")
        else:
            other_account.deposit(amount)
            self.balance -= amount
            self.transaction_history.append(f"Transferred: {amount} to {other_account.name}")
            other_account.transaction_history.append(f"Received: {amount} from {self.name}")
            print("Transfer completed successfully")  # Moved inside the else block

class Admin(AsiaBank):
    def __init__(self):
        self.users = []

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.users.append(user)

    def delete_account(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.users.remove(user)
                print("Account deleted ")
                return
        print("Account not found")

    def view_all_accounts(self):
        for user in self.users:
            print(f"Name: {user.name}, Email: {user.email}, Account Type: {user.account_type}")

    def total_balance(self):
        total_balance = sum(user.balance for user in self.users)
        print(f"Total balance of the bank: {total_balance}")

    def total_loan_amount(self):
        total_loan = sum(user.loan_taken for user in self.users)
        print(f"Total loan amount: {total_loan}")

    def activation_loan(self, status):
        AsiaBank.bank_loan_possible = False if status == "off" else True
        print(f"Loan feature is now {status}")

admin = Admin()

print("Asia Bank Limited")

while True:
    print("###########")
    print("1. User Menu")
    print("2. Admin Menu")
    print("3. Exit")
    option = input("Enter Option: ")
    print("###########")

    if option == "1":
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Check Transaction History")
        print("6. Take Loan")
        print("7. Transfer Money")
        user_option = input("Enter Option: ")

        if user_option == "1":
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            account_type = input("Enter Account Type (Savings or Current): ")
            admin.create_account(name, email, address, account_type)
            print(f"Account created successfully with Account Number: {admin.users[-1].account_number}")

        elif user_option == "2":
            account_number = int(input("Enter Account Number: "))
            amount = float(input("Enter Amount to Deposit: "))
            for user in admin.users:
                if user.account_number == account_number:
                    user.deposit(amount)
                    print("Amount deposited successfully")
                    break
            else:
                print("Account not found")

        elif user_option == "3":
            account_number = int(input("Enter Account Number: "))
            amount = float(input("Enter Amount to Withdraw: "))
            for user in admin.users:
                if user.account_number == account_number:
                    user.withdraw(amount)
                    break
            else:
                print("Account not found")

        elif user_option == "4":
            account_number = int(input("Enter Account Number: "))
            for user in admin.users:
                if user.account_number == account_number:
                    balance = user.check_balance()
                    print(f"Balance for account {account_number}: {balance}")
                    break
            else:
                print("Account not found")

        elif user_option == "5":
            account_number = int(input("Enter Account Number: "))
            for user in admin.users:
                if user.account_number == account_number:
                    transaction_history = user.check_transaction_history()
                    print(f"Transaction History for account {account_number}:")
                    for transaction in transaction_history:
                        print(transaction)
                    break
            else:
                print("Account not found")

        elif user_option == "6":
            account_number = int(input("Enter Account Number: "))
            amount = float(input("Enter Loan Amount: "))
            for user in admin.users:
                if user.account_number == account_number:
                    user.take_loan(amount)
                    print("Loan taken successfully")
                    break
            else:
                print("Account not found")

        elif user_option == "7":
            sender_account_number = int(input("Enter Sender's Account Number: "))
            receiver_account_number = int(input("Enter Receiver's Account Number: "))
            amount = float(input("Enter Amount to Transfer: "))
            sender = None
            receiver = None
            for user in admin.users:
                if user.account_number == sender_account_number:
                    sender = user
                if user.account_number == receiver_account_number:
                    receiver = user
                if sender and receiver:
                    break
            else:
                print("One or both accounts not found")
                continue

            sender.transfer(amount, receiver)

    elif option == "2":
        print("1. Create Account")
        print("2. Delete Account")
        print("3. View All Accounts")
        print("4. Total Balance")
        print("5. Total Loan Amount")
        print("6. Activation Loan Feature")
        admin_option = input("Enter Option: ")

        if admin_option == "1":
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            account_type = input("Enter Account Type (Savings or Current): ")
            admin.create_account(name, email, address, account_type)
            print(f"Account created successfully with Account Number: {admin.users[-1].account_number}")

        elif admin_option == "2":
            account_number = int(input("Enter Account Number to delete: "))
            admin.delete_account(account_number)

        elif admin_option == "3":
            admin.view_all_accounts()

        elif admin_option == "4":
            admin.total_balance()

        elif admin_option == "5":
            admin.total_loan_amount()

        elif admin_option == "6":
            status = input("Enter 'on' to enable or 'off' to disable loan feature: ")
            admin.activation_loan(status)

        else:
            print("Invalid option. Please choose again.")

    elif option == "3":
        break

    else:
        print("Invalid option. Please choose again.")
