class Account:
  def __init__(self, name):
    self.name = name
    self.balance = 0
    self.deposits = []
    self.withdrawals = []


  def make_deposit(self, amount):
    self.deposits.append(amount)
    self.balance += amount
    return f"Hello {self.name}, you have received {amount}. Your new balance is {self.balance}"


  def make_withdrawal(self, amount):
    if amount <= self.balance:
        self.withdrawals.append(amount)
        self.balance -= amount
        return f"Hello {self.name}, you have withdrawn {amount}. Your new balance is {self.balance}"
    else:
        return "Insufficient funds for withdrawal"


  def get_balance(self):
    return self.balance


  def transfer(self, amount):
    if self.balance >= amount:
      self.balance -= amount
      self.withdrawals.append(amount)
      return "Transfer successful."
    else:
        return "Transfer failed: Insufficient funds or invalid amount."


  def request_loan(self, amount, loan_balance):
    loan_balance = 0
    if amount > 0 :
      loan_balance += amount
      print(f"Loan of ${amount} requested. Current loan balance: ${loan_balance}")
    else:
      print("Invalid loan amount")


  def pay_loan(self, amount, loan_balance):
    if 0 < amount <= loan_balance:
      loan_balance -= amount
      self.balance -= amount
      print(f"Loan payment of ${amount} processed. Remaining loan balance: ${loan_balance}. New account balance: ${self.balance}")
    elif amount > loan_balance:
      print(f"Loan payment exceeds loan balance. Current loan balance: ${loan_balance}")
    else:
      print("Invalid loan payment amount.")


  def account_details(self):
    return f"Hello {self.name}, your account balance is {self.balance}"  

  
  def get_statement(self): 
    return f"Hello {self.name} your debt is fully settled"


  def get_loan_statement(self,amount):
    return f"Hello {self.name} you have received {amount} loan"


  def change_account_owner(self, new_name):
    self.name == new_name
    return new_name


  def account_statement(self):
    print(f"Hello {self.name}, you have received {sum(self.deposits)} and withdrawn {sum(self.withdrawals)}. Your account balance is {self.balance}")


  def account_statement(self):
    total_deposits = 0
    total_withdrawals = 0
    for deposit in self.deposits:
      total_deposits + deposit
    for withdrawal in self.withdrawals:
      total_withdrawals += withdrawal
      self.balance = total_deposits - total_withdrawals
      print (f"Hello {self.name}, you have received {total_deposits} and withdrawn {total_withdrawals}. Your account balance is {self.balance}")


  def interest_calculations(self, principal, time):
    rate = 0.05 
    interest = principal * rate * time
    return interest


  def unfreeze(self, is_freeze):
    if is_freeze == "true":
      return f"Your account has been frozen."
    else:
      return f"Your account is unfrozen."


  def set_minimum_balance(self, amount):
    min_amount = 300
    if self.balance - amount >= min_amount:
      self.balance -= amount
      return self.balance
    else:
      return f"You cannot withdraw if your balance is less than {min_amount}."


  def close_account(self, account_id, accounts, transactions):
    for account in accounts:
      if account_id == account.account_id:
        accounts.remove(account)
        transactions = [t for t in transactions if t.account_id != account_id]
        return f"Account with ID {account_id} not found."


  










