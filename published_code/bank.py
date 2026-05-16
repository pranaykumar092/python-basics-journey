def show_balance(balance):
    print("|------------------------------|")
    print(f"Your Balance is {balance:.2f}")
    print("|------------------------------|")

def depodit():
    print("|------------------------------|")
    amount = float(input("Enter amount to be deposited: "))
    print("|------------------------------|")

    if amount < 0:
        print("|------------------------------|")
        print("That is not valid")
        print("|------------------------------|")
    else:
        return amount    

def withdraw(balance):
    print("|------------------------------|")
    amount = float(input("Enter amount to be withdrawn: "))
    print("|------------------------------|")

    if amount > balance:
        print("|------------------------------|")
        print("Insufficient balance")
        print("|------------------------------|")
        return 0

    elif amount < 0:
        print("|------------------------------|")
        print("Amount must be greater than 0")
        print("|------------------------------|")
        return 0

    else:
        return amount

def main ():
    balance = 0
    is_running = True

    while is_running:
        print("|------------------------------|")
        print("Banking Program")
        print("1. To check Balance")
        print("2. To deposit Money")
        print("3. To withdraw money")
        print("4. Exit")
        print("|------------------------------|")
        print()

        choice = input("Enter your choice from (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += depodit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("Not a Valid choice.")

    
    print("|------------------------------|")
    print("Thank you for banking with us. :) ")
    print("|------------------------------|")

if __name__ == '__main__':
    main()