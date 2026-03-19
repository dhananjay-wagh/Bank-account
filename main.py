from blueprint import SavingsAccount
from blueprint import InsufficientFundsError
from blueprint import NegativeTransactionError
from pathlib import Path

file_location = "User_details.txt"
file_location_path = Path(file_location)

if not file_location_path.exists():
    file_location_path.touch()

is_empty = file_location_path.stat().st_size == 0


def get_user_info():
    while True:
        user_name = input("Enter Your Name : ")
        confirm_name = input("The name you entered is correct (y/n) : ")
        if confirm_name.lower() == 'y':
            break
        else:
            continue

    while True:
        try:
            initial_balance = int(input("Enter initial balance : $"))
            break
        except ValueError as e:
            print(f"Error :{e}")

    while True:
        try:
            interest_rate = float(input("Enter Interest rate : "))
            break
        except ValueError as e:
            print(f"Error : {e}")
    return [user_name , initial_balance , interest_rate]


import_info = input("Do you want to import previous info (y/n) : ")
user_info_list = []

if import_info.lower() == 'y':
    if is_empty:
        print("File is Empty , please fill the user information : ")
        user_info_list = get_user_info()
        user_name, initial_balance, interest_rate = user_info_list
    else:
        with open(file_location) as f:
            lines = f.readlines()
            user_info_list = [ line.strip() for line in lines]
        user_name, initial_balance, interest_rate = user_info_list

else:
    user_info_list = get_user_info()
    user_name, initial_balance, interest_rate = user_info_list

initial_balance = int(initial_balance)
interest_rate = float(interest_rate)
user = SavingsAccount(user_name , initial_balance , interest_rate)

while True:
    menu = input("1. Get Balance \n2. Withdraw Amount \n3. Deposit Amount \n4. Get account info \nq to quit \nEnter Input : ")

    if menu == '1':
        print(f"Balance : ${user.get_balance()}")
    
    elif menu == '2':
        while True:
            try:
                withdraw_amount = int(input("Enter amount you want to withdraw : $ "))
                break
            except ValueError as e:
                print(f"Error : {e}")
        try:
            print(f"${withdraw_amount} Withdraw Successful - Remaining Balance: ${user.withdraw(withdraw_amount)}")
        except (InsufficientFundsError, NegativeTransactionError):
            pass

    elif menu == '3':
        while True:
            try:
                deposit_amount = int(input("Enter amount you want to Deposit : $ "))
                break
            except ValueError as e:
                print(f"Error : {e}")
        try:
            print(f"${deposit_amount} Deposit Successful - Remaining Balance: ${user.deposit(deposit_amount)}")
        except (InsufficientFundsError, NegativeTransactionError):
            pass


    elif menu == '4':
        print(f"{user.to_json()}")

    elif menu.lower() == 'q':
        user_info_list = [ user_name , user.get_balance(), interest_rate]
        with open(file_location, 'w') as f:
            for item in user_info_list:
                f.write(f"{item}\n")
        break
    else:
        print("Invalid Input!!")