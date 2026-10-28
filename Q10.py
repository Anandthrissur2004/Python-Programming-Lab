#Program to create a BankAccount class with attributes such as account
#number, account holder name, account type, and balance
class BankAccount:

    def __init__(self, account_number, account_holder_name, account_type, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount credited: {amount}.\n New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Amount withdrawn: {amount}.\n New balance: {self.balance}")

    def display_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder Name: {self.account_holder_name}")
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: {self.balance}")


account1 = int(input("Enter Account number: "))
account_holder_name = input("Enter Account holder name: ")
account_type = input("Enter Account type: ")
initial_balance = float(input("Enter initial balance: "))

account = BankAccount(account1, account_holder_name, account_type, initial_balance)

while True:
    print("\n==============================================================")
    print("\nAccount Details:")
    print("1.Deposit")  
    print("2.Withdraw")
    print("3.Display Account Details")
    print("4.Exit")

    choice = int(input("\nEnter your choice (1-4): "))

    match choice:
        case 1:
            amount = float(input("Enter Amount to deposit: "))
            account.deposit(amount)

        case 2:
            amount = float(input("Enter Amount to withdraw: "))
            account.withdraw(amount)
        case 3:
            account.display_account_details()
        case 4:
            print("Exiting the program.")
            break
        case _:
            print("Invalid choice. Please select a valid option.")

    



    

    