from datetime import datetime

class Transaction:
  def __init__(self, date_time, narration, amount, transaction_type):
    self.date_time = date_time
    self.narration = narration
    self.amount = amount
    self.transaction_type = transaction_type

  def __repr__(self):
    return (f"Transaction({self.date_time}, {self.narration}, "
    f"{self.amount}, {self.transaction_type})")


class Account:
  def __init__(self, account_id, name):
    self.__account_id = account_id
    self.__name = name
    self.__transactions = []
    self.balance = 0
    self._is_freeze = "true"

  def get_account_id(self):
    return self.__account_id
  
  
  def get_account_name(self):
    return self.__name

  def change_account_owner(self, new_name):
    self.__name = new_name
    return self.__name

  def make_deposit(self, amount, narration="Deposit"):
    transaction = Transaction(datetime.now(), narration, amount, 'credit')
    self.__transactions.append(transaction)
    return transaction

  def get_balance(self):
    balance = 0
    for txn in self.__transactions:
        if txn.transaction_type == 'credit':
            balance += txn.amount
        elif txn.transaction_type == 'debit':
            balance -= (txn.amount)
    return balance

  def make_withdrawal(self, amount, narration="Withdrawal"):
    if amount <= self.get_balance():
        transaction = Transaction(datetime.now(), narration, -amount, 'debit')
        self.__transactions.append(transaction)
        return transaction
    else:
        print("Insufficient funds for withdrawal.")

  def get_all_transactions(self):
    return self.__transactions.copy()

  def transfer(self, amount):
    if amount <= self.get_balance():
      transaction = Transaction(datetime.now(), "Transfer", -amount, 'debit')
      self.__transactions.append(transaction)
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
    if amount <= self.get_balance():
        transaction = Transaction(datetime.now(), "Loan payment", -amount, 'debit')
        self.__transactions.append(transaction)
        return f"Loan payment of ${amount} processed successfully."
    else:
        return "Insufficient funds for loan payment."


  def account_details(self):
    return f"Hello {self.__name} Account ID: {self.__account_id}, your Total Transactions: {len(self.__transactions)} and Account Status: Active "
    

  def account_statement(self):
    total_deposits = sum(txn.amount for txn in self.__transactions if txn.transaction_type == 'credit')
    total_withdrawals = sum(-txn.amount for txn in self.__transactions if txn.transaction_type == 'debit')
    print(f"Hello {self.__name}, total deposited: {total_deposits}, total withdrawn: {total_withdrawals}. Current balance: {self.get_balance()}")

  def unfreeze(self, is_freeze):
    if is_freeze == "true":
      return "Your account has been frozen."
    else:
      return "Your account is unfrozen."

  def set_minimum_balance(self, amount):
    min_amount = 300
    current_balance = self.get_balance()
    if current_balance - amount >= min_amount:
      self.make_withdrawal(amount, "Set Minimum Balance Deduction")
      return self.get_balance()
    else:
      return f"You cannot withdraw if your balance is less than {min_amount}."

  def close_account(self, account_id, accounts):
    for account in accounts:
        if account.get_account_id() == account_id:
            accounts.remove(account)
            return f"Account {account_id} has been successfully closed."
    return f"Account with ID {account_id} not found."


