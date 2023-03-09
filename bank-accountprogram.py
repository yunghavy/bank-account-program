# Bank account
# balance, accno, name, branch active
print("        ")
print("KCB BANK ACCOUNT")


class Account:
    bank_code = 1000

    def __init__(self, balance, accno, name, branch, status):
        if balance < 0:
            print("Balance cannot be zero")
        elif len(name) == 0:
            print("Please enter your name")
        elif len(accno) != 11:
            print("Invalid account number")
        else:
            print("Bank details captured")
            self.balance = balance
            self.accno = accno
            self.name = name
            self.branch = branch
            self.status = status

    def check_balance(self):
        print(f'You balance is {self.balance}')
        return self.balance

    def deposit(self, cash_deposit):
        if cash_deposit <= 0:
            print("Cannot deposit zero or negative amount")
        elif cash_deposit > 100000:
            print("You have exceeded the maximum deposit amount")
        else:
            if self.status == "active":
                print("Thank you for depositing with us")
                print(f'Your previous balance was {self.check_balance()}')
                self.balance = self.balance + cash_deposit
                print(f'Your current balance is {self.balance}')

            else:
                print("Your account is inactive")

    def withdraw(self):
        initial_deposit = 1000
        cash_withdraw = int(input("Enter amount to withdraw"))

        if cash_withdraw > self.balance:
            print("You have insufficient balance")
        elif self.status == "inactive":
            print("Sorry, you have an inactive account!")

        else:
            if self.status == "active":
                print("Transaction was successful")
                print("Amount withdrawn is {}".format(cash_withdraw))
                self.balance = self.balance - cash_withdraw
                print("Your balance is {}".format(self.balance))
                return self.balance
            else:
                print("Please visit the nearest branch near you")
    
    def transfer(self, recipient_account, amount):
        if amount <= 0:
            print("Cannot transfer zero or negative amount")
        elif amount > self.balance:
            print("You have insufficient balance")
        else:
            self.balance -= amount
            recipient_account.balance += amount
            print(f"Transfer of KES {amount} successful to account {recipient_account.accno}")
            print(f"Your new balance is {self.balance}")

    def calculate_interest(self, rate):
        interest = self.balance * rate /100
        print(f"Interest earned is KES {interest:2f}")
    
    def display_details(self):
        print("Account details:")
        print(f"Account number: {self.accno}")
        print(f"Name: {self.name}")
        print(f"Branch: {self.branch}")
        print(f"Balance: {self.balance}")

account1 = Account(1000, "12345678910", "Washington", "Ngara", "active")
account1.display_details()
account1.check_balance()
account1.deposit(1500)
account1.withdraw()
account2 = Account(500, "10987654321", "Adams", "Westlands", "active")
account1.transfer(account2, 500)
account1.calculate_interest(5)

account1.deposit(1500)
account1.withdraw()
