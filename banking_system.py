#BANKING SYSTEM SIMULATION#
class Account:
    def __init__(self, id, holder_name):
        self.id = id
        self.holder_name = holder_name
        self._balance = 0
    def check_balance(self):
        print(f"Balance: {self._balance}")
    def deposit(self, amount):
        self._balance +=amount
        print(f"Deposit Successful. Updated Balance: {self._balance}")
    def withdraw(self, amount):
        if self._balance>=amount:
            self._balance -=amount
            print(f"Withdraw Successful. Updated Balance: {self._balance}")
        else:
            print("Insufficient Balance")
            
class S_Account(Account):
    
    def calc_interest(self):
        interest_rate = 0.04
        interest = self._balance *interest_rate
        print(f"Interest:{interest}")
class C_Account(Account):
    def withdraw(self, amount):
        overdraft_limit = 1000
        if self._balance + overdraft_limit>=amount:
            self._balance -=amount
            print(f"Withdraw Successful. Updated Balance: {self._balance}")
        else:
            print("Insufficient Balance")
    
class Bank:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.__account = {}
    def create_account(self, id, holder_name, type):
        if type=="Savings":
            new_account = S_Account(id, holder_name)
        elif type=="Current":
            new_account =C_Account(id, holder_name)
        self.__account[id] = new_account
        print("Account creation successful")
        return new_account
    def get_account(self, id):
        if id not in self.__account:
            print("Account not found")
            return None
        else:
            account = self.__account[id]
            print(f"\nID: {account.id}\nHolder Name: {account.holder_name}")
            return account
sbi = Bank("State Bank of India", "Udupi")
a1 = sbi.create_account("1", "ABC", "Savings")
a2 = sbi.create_account("2", "DEF", "Current")
a1.deposit(1000)
a2.deposit(10)
a1.withdraw(2000)
a2.withdraw(20)
a1.calc_interest()
a1.check_balance()
a2.check_balance()

