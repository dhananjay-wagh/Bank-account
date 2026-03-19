import json

class NegativeTransactionError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

def transaction_logger(func):
    def wrapper( *args , **kwargs):
        print("[AUDIT] Processing transaction...")
        try:
            result = func(*args,**kwargs)
            print("[AUDIT] Transaction successful.")
            return result
        except (NegativeTransactionError , InsufficientFundsError) as e:
            print(f"Error : {e}")
            raise
    return wrapper

class BankAccount:
    def __init__(self , account_holder , initial_balance):
        self.account_holder = account_holder
        self.__initial_balance = initial_balance

    @transaction_logger
    def deposit(self, amount):
        if amount < 0:
            raise NegativeTransactionError("Negative Balance cannot be deposited in the account")
        else:
            self.__initial_balance += amount
            return self.__initial_balance
    @transaction_logger
    def withdraw( self, amount):
        if amount < 0:
            raise NegativeTransactionError("Cannot withdraw Negative amount!")
        elif amount > self.__initial_balance:
            raise InsufficientFundsError("Insufficient Funds")
        else:
            self.__initial_balance -= amount
            print(f"${amount} withdraw successful!")
            return self.__initial_balance

    def get_balance(self):
        return self.__initial_balance

    def __str__(self):
        return f"BankAccount: {self.account_holder} - Balance: ${self.__initial_balance}"
    
    def to_json(self):
        to_dict = {
            "Name": self.account_holder,
            "Current Balence": self.__initial_balance
        }
        return json.dumps(to_dict, indent=4)
    
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance, interest_rate):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate
    


if __name__ == "__main__":
    user = SavingsAccount("Dhananjay" , 1000, 1.55)
    print(user.withdraw(500))