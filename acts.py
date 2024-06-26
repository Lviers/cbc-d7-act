


from random import randint

def main():
    balance = 0
    is_running = True
    
    print("Welcome to Epstein Banking")
    username = input("Enter username: ")
    user_id = randint(0000, 9999)  
    usernames = f"{username} user_id:  {user_id}" 
    
    while is_running:

        print("\n  Epstein Banking   ")
        print(" ",usernames)
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Delete Account")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            show_balance( username, balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("Again")

    print("Account Deleted")

def show_balance(username, balance):
    print(f"Hey {username}, your balance is P{balance:.2f}")


def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount


if __name__ == '__main__':
    main()
"""
name = ("username: ")
password = ("password: ")
acc = {}
def create():
    if name == name and password == password:
        acc.insert(name)
        acc.insert(password)
        name = randint(0,1000)
    ()"""

