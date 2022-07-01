class BankAccount:
  
  all_accounts = []
  
  def __init__( self, int_rate, balance, first_name ):
    self.int_rate = int_rate
    self.balance = balance
    self.first_name = first_name
    BankAccount.all_accounts.append(self)
    
  def deposit( self, amount ):
    self.balance += amount
    return self
  
  
  def withdraw(self, amount):
    if (self.balance < amount):
      self.balance -= 5
      print("\n Insufficient funds: Charging a $5 fee ")
      return self
    else:
      self.balance -= amount
      return self
  
  def display_account_info(self):
    print( f"Balance: ${self.balance}" )
    return self

  def yield_interest(self):
    calculated_rate = self.balance * self.int_rate
    self.balance = self.balance + calculated_rate
    return self

  @classmethod
  def Accounts(cls):
    for account in cls.all_accounts:
      print(account.first_name+ "'s balance is: ", account.balance)


froilan = BankAccount( 0.01, 50, "Froilan")
froilan.deposit(100).display_account_info().withdraw(200).display_account_info().yield_interest().display_account_info()

print('--------')

diane = BankAccount( 0.01, 0, "Diane")
diane.deposit(100).display_account_info().deposit(500).display_account_info().deposit(1000).display_account_info().withdraw(800).display_account_info().yield_interest().display_account_info()

print('---------')

luffy = BankAccount( 0.01, 0, "Luffy")
luffy.deposit(900000).display_account_info().withdraw(10000).withdraw(90000).display_account_info().deposit(1000000).display_account_info().withdraw(100000).display_account_info().withdraw(800000).display_account_info().yield_interest().display_account_info()

print('-----')


BankAccount.Accounts()