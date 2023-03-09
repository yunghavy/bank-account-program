# Bank account
# balance, accno, name, branch active

print("        ")
print("JAKIKI BANK ACCOUNT")

import smtplib

class Account:
    bank_code = 1000

    def __init__(self, balance, accno, name, branch, status, email=None, phone=None):
        
        if balance < 0:
            print("Balance cannot be zero")
        elif len(name) == 0:
            print("Please enter your name")
        elif len(accno) != 11:
            print("Invalid account number")
        elif not isinstance(status, str) or status not in ["active", "inactive"]:
            print("Invalid account status")
        else:
            print("Bank details captured")
            self.balance = balance
            self.accno = accno
            self.name = name
            self.branch = branch
            self.status = status
            self.email = email
            self.phone = phone

    def send_notification(self, message):
        if self.email:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('your_email@example.com', 'your_password')
            server.sendmail('your_email@example.com', self.email, message)
            server.quit()

        if self.phone:
            # To add a third-party SMS gateway to send the message to the user's phone
            
            pass


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
                self.send_notification(f"Dear {self.name}, your account has been credited with KES {cash_deposit}.")
                print(f'Your current balance is {self.balance}')

            else:
                print("Your account is inactive")
        

    def withdraw(self):
        initial_deposit = 1000
        cash_withdraw = int(input("Enter amount to withdraw"))

        try:
            cash_withdraw = int(cash_withdraw)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return

        if cash_withdraw > self.balance:
            print("You have insufficient balance")
        elif self.status == "inactive":
            print("Sorry, you have an inactive account!")

        else:
            if self.status == "active":
                print("Transaction was successful")
                print("Amount withdrawn is {}".format(cash_withdraw))
                self.balance = self.balance - cash_withdraw
                self.send_notification(f"Dear {self.name}, your account has been debited with KES {cash_withdraw}. Your current balance is KES {self.balance}.")
                print("Your balance is {}".format(self.balance))
                return self.balance
            else:
                print("Please visit the nearest branch near you")
    
    def transfer(self, amount, recipient):
        if not isinstance(amount, (int, float)):
            print("Invalid input: Amount should be numeric.")
            return

        if amount <= 0:
            print("Invalid input: Amount should be positive.")
            return

        if len(recipient.accno) != 11:
            print("Invalid input: Invalid account number for recipient.")
            return

        if self.status == "inactive":
            print("Sorry, you have an inactive account!")
            return

        if self.balance < amount:
            print("You have insufficient balance.")
            return

        if self.status == "active" and recipient.status == "active":
            print("Transaction was successful.")
            self.balance -= amount
            recipient.balance += amount
            print(f"Your new balance is {self.balance}")
            return self.balance
        else:
            print("One or both accounts are inactive.")

    def change_details(self, name=None, branch=None):
        if name:
            self.name = name
            print("Account name updated successfully!")
        if branch:
            self.branch = branch
            print("Account branch updated successfully!")

    def interest_earned(self, rate):
        interest = self.balance * rate / 100
        print(f"Interest earned on balance of {self.balance} at {rate}% is {interest}")
    
    def account_details(self):
        print(f"Account Number: {self.accno}")
        print(f"Account Name: {self.name}")
        print(f"Branch: {self.branch}")
        print(f"Balance: {self.balance}")
        print(f"Status: {self.status}")

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
