

from datetime import datetime

class Transaction:
    def __init__(self, date_time, narration, amount, transaction_type):
        self.date_time = date_time
        self.narration = narration
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return (f"{self.date_time} | {self.transaction_type} | "
                f"{self.narration} | Amount: {self.amount}")

class Account:
    def __init__(self, name, account_id):
        self.name = name
        self.__account_id = account_id    
        self.__balance = 0                  
        self.deposits = []
        self.withdrawals = []
        self.transactions = []
        self.is_freeze = "False"
        self.loan_balance = 0

    def get_account_id(self):
        return self.__account_id


    def get_balance(self):
        return self.__balance


    def __add_transaction(self, narration, amount, transaction_type):
        transaction = Transaction(datetime.now(), narration, amount, transaction_type)
        self.transactions.append(transaction)

    def make_deposit(self, amount):
        self.__balance += amount
        self.deposits.append(amount)
        self.__add_transaction(f"Deposit of {amount}", amount, "Deposit")
        return f"Hello {self.name}, you have received {amount}. Your new balance is {self.get_balance()}"

    
    def make_withdrawal(self, amount):
        if self.is_freeze:
            return "Account is frozen. Cannot perform withdrawal."
        if amount <= self.__balance:
            self.__balance -= amount
            self.withdrawals.append(amount)
            self.__add_transaction(f"Withdrawal of {amount}", amount, "Withdrawal")
            return f"Hello {self.name}, you have withdrawn {amount}. Your new balance is {self.get_balance()}"
        else:
            return "Insufficient funds for withdrawal"

    def transfer(self, amount):
        if self.is_freeze:
            return "Account is frozen. Cannot perform transfer."
        if self.__balance >= amount:
            self.__balance -= amount
            self.__add_transaction(f"Transfer of {amount}", amount, "Transfer")
            return "Transfer successful."
        else:
            return "Transfer failed: Insufficient funds or invalid amount."

    def request_loan(self, amount):
        current_balance = self.get_balance()
        if current_balance < 500:
            return "Loan request denied: Insufficient account balance."
        elif amount > 2 * current_balance:
            return "Loan request denied: Requested amount exceeds the loan limit based on your current balance."
        else:
            transaction = Transaction(datetime.now(), "Loan approved", amount, 'credit')
            self.__transactions.append(transaction)
            return f"Loan of ${amount} approved and credited to your account."


    def pay_loan(self, amount):
        if amount > 0 and amount <= self.loan_balance:
            self.__balance -= amount
            self.loan_balance -= amount
            self.__add_transaction(f"Loan payment of {amount}", amount, "Loan Payment")
            return f"Loan payment of ${amount} processed. Remaining loan balance: ${self.loan_balance}. New account balance: ${self.get_balance()}"
        elif amount > self.loan_balance:
            return f"Loan payment exceeds loan balance. Current loan balance: ${self.loan_balance}"
        else:
            return "Invalid loan payment amount."

    def account_details(self):
        return f"Hello {self.name} Account ID: {self.__account_id}, your Total Transactions: {len(self.transactions)} and Account Status: Active "


    def account_statement(self):
        total_deposits = sum(self.deposits)
        current_balance = self.get_balance()
        return (f"Hello {self.name}, total deposits: {total_deposits}, "
                f"current balance: {current_balance}")

    def change_account_owner(self, new_name):
        self.name = new_name
        return new_name

    def unfreeze(self, freeze_status):
        self.is_freeze = freeze_status
        if self.is_freeze:
            return "Your account has been frozen."
        else:
            return "Your account is unfrozen."

    def set_minimum_balance(self, amount):
        min_balance = 300
        if self.__balance - amount >= min_balance:
            self.__balance -= amount
            self.__add_transaction(f"Withdrew {amount} for minimum balance", amount, "Withdrawal")
            return self.get_balance()
        else:
            return f"You cannot withdraw if your balance is less than {min_balance}."

    def close_account(self, account_list):
        for account in account_list:
            if account.get_account_id() == self.__account_id:
                account_list.remove(account)
                return f"Account with ID {self.__account_id} closed."
        return "Account not found."

