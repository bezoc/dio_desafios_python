def menu():
   menu_text = """\n
   ========== PLEASE SELECT A TRANSACTION  ==========

   [1] - Deposit
   [2] - Withdrawal
   [3] - Bank Statement
   [4] - New Account
   [5] - Other Accounts
   [6] - New User
   [0] - Exit

   ===================================================
   """
   return menu_text
   
def deposit(balance, amount, statement, /):
     if amount > 0:
            balance += amount
            statement += f"Deposit: $ {amount:.2f}\n"
            print("\n==== Deposit Successful ====")
            
     else:
            print("== Deposit failed! ==")
         
     return balance, statement   
      
def withdrawal(*, balance, amount, statement, limit, withdrawal_qty, withdrawal_limit):
   exceed_balance = amount > balance
   exceed_limit = amount > limit
   exceed_withdrawals = withdrawal_qty >= withdrawal_limit
   
   if exceed_balance:
      print("\n== Your transaction failed! You don't have enough balance! ==")
   
   elif exceed_limit:
      print("\n== Your transaction failed! You've exceeded your withdrawal amount limit. ==") 
      
   elif exceed_withdrawals:
      print("\n== Your transaction failed! You've exceeded your withdrawal limit. ==")       
      
   elif amount > 0:
      balance -= amount
      statement += f"Withdrawal: $ {amount:.2f}\n"
      withdrawal_qty += 1
      print("\n==== Withdrawal successful! ==== ")
      
   else:
      print("\n== Your transaction failed! Invalid amount. ==")
      
   return balance, statement
   

def show_statement(balance, /, *, statement):
  print("\n ========== BANK STATEMENT ==========")
  print("No transactions yet." if not statement else statement)
  print(f"\nBalance: R$ {balance:.2f}")
  print("=======================================")       
            
def create_user(users):
   id = input("Please inform your ID (Numbers only): ")
   user = filter_user(id, users)
   
   if user:
      print("\n == User already exists! ==") 
      return
   
   name = input("Inform your full name: ")
   birthday = input("What is your date of birth (dd-mm-aaaa): ")
   address = input("Please, inform your full address: ")
   
   users.append({"name": name, "date_birth": birthday, "id": id, "address": address})
   
   print("==== User successfully created! ====")
   

def filter_user(id, users):
   filtered_users = [user for user in users if user["id"] == id]
   return filtered_users[0] if filtered_users else None

def new_account(agency, account_id, users):
   id = input("Please, inform the user ID: ")
   user = filter_user(id, users) 
   
   if user:
      print("\n ==== Congratulations, your account has been successfully created! ====")
      return {"agency": agency, "account_id": account_id, "user": user}
   
   print("\n == User not found. ==")
   
def list_accounts(accounts):
   for account in accounts:
      line = f"""\
Agency:\t{account['agency']}
ACCT:\t\t{account['account_id']}
Account Holder:\t{account['user']['name']}
"""
      print("=" * 40)
      print(line)
      print("=" * 40)                 
         
      
def main():
    AGENCY = "0001"
    users = []
    accounts = []
    balance = 2000
    limit = 500
    statement = ""
    withdrawal_qty = 0
    CASH_LIMIT = 3
    
    while True:
       option = input(menu())
       
       if option == '1':
          amount = float(input("Please specify deposit amount: "))
          
          balance, statement = deposit(balance, amount, statement)
          
       elif option == '2':
          amount = float(input("Withdrawal Amount: "))
          balance, statement = withdrawal(
             balance=balance,
             amount=amount,
             statement=statement,
             limit=limit,
             withdrawal_qty=withdrawal_qty,
             withdrawal_limit=CASH_LIMIT
            )
          
       elif option == '3':
           show_statement(balance, statement=statement)
                
       elif option == '4':
            account_id = len(accounts) + 1
            account = new_account(AGENCY, account_id, users)
            
            if account:
               accounts.append(account)
         
       elif option == '5':
            list_accounts(accounts)
            
         
       elif option == '6': 
            create_user(users)
                    
       elif option == '0':
            break
                    
       else:
          
          print("Invalid transaction. Please, choose another option.")
   
main()            