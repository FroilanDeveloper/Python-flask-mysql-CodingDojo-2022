class BankAccount:
  
  all_accounts = []
  
  def __init__( self, int_rate, balance ): # Constructor
    self.int_rate = int_rate   # This are called Instance variables/Constructor variables
    self.balance = balance

    BankAccount.all_accounts.append(self)
    
  def deposit( self, amount ): 
    self.balance += amount # Which adds amount to my bankaccount
    return self # return the instance that I created to bank account 
  
  def withdraw(self, amount):
    if (self.balance < amount):
      self.balance -= 5 # Just means to deduct $5 to bank account if withdrawing more than the balance 
      print("\n Insufficient funds: Charging a $5 fee ")
      return self
    else:
      self.balance -= amount # Remove the amount from balance 
      return self
  
  def display_account_info(self): #this just means to show the output of the current balance
    print( f"Balance: ${self.balance}" )
    return self

  def yield_interest(self): 
    self.balance += (self.balance * self.int_rate) #shoter way # This means balance * intrest rate + balance, i would get the current balance
    # self.balance = self.balance + calculated_rate longer way    # += means define variable and add variable
    return self

  @classmethod
  def showAccounts(cls):  #This means to use all instances of bank account #functions example = getAccounts, showAccount
    for account in cls.all_accounts:  
      print(account.first_name+ "'s balance is: ", account.balance)  #show 

# BankAccount.showAccounts()


class User:
  
  all_users = [] #global variable 
  
  def __init__(self, first_name):
    self.first_name = first_name 
    self.account = BankAccount( 0.02, 0) #this is connecting the class BankAccount with the class User
    User.all_users.append(self) # append  this to all user
    

  def display_user_balance(self):
    print(f"User: {self.first_name}'s balance is ${self.account.balance}" )
    return self


  @classmethod
  def all_user_balance(cls):
    print("ALL USERS BALANCES")
    for each_user in cls.all_users:
      print(f"{each_user.first_name}'s Balance is ${each_user.account.balance}" )  # This just means to print all users balances 


zoro = User("Zoro")
chopper = User("Chopper")

zoro.account.deposit(9000532).withdraw(293414)
zoro.display_user_balance()

chopper.account.deposit(100)
chopper.display_user_balance()

print('------')

User.all_user_balance()