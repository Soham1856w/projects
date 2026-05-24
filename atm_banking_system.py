# this is banking system
print("Welcome to banking system")
def create_account():
    name = input("Enter your name: ")
    pin = input("Set 4-digit PIN: ")
    balance = 0
    print("\nAccount Created Successfully!")
    return name, pin, balance


def deposit(balance):
    amount = float(input("Enter deposit amount: "))
    balance += amount
    print("Amount Deposited Successfully!")
    return balance


def withdraw(balance):
    amount = float(input("Enter withdraw amount: "))
    
    if amount <= balance:
        balance -= amount
        print("Please collect your cash.")
    else:
        print("Insufficient Balance!")
    
    return balance


def check_balance(balance):
    print("Your Current Balance is:", balance)


def change_pin(pin):
    old_pin = input("Enter old PIN: ")
    
    if old_pin == pin:
        new_pin = input("Enter new PIN: ")
        print("PIN Changed Successfully!")
        return new_pin
    else:
        print("Wrong PIN!")
        return pin


def main():
    name, pin, balance = create_account()

    while True:
        print("\n===== BANK MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                balance = deposit(balance)

            case "2":
                entered_pin = input("Enter PIN: ")
                if entered_pin == pin:
                    balance = withdraw(balance)
                else:
                    print("Wrong PIN!")

            case "3":
                entered_pin = input("Enter PIN: ")
                if entered_pin == pin:
                    check_balance(balance)
                else:
                    print("Wrong PIN!")

            case "4":
                pin = change_pin(pin)

            case "5":
                print("Thank you for using our bank,", name)
                break

            case _:
                print("Invalid Choice!")


if __name__ == "__main__":
    main()