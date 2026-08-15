# ========= ATM =========


pin=int(input("Enter your pin: "))

for attempt in range(1,4):
    if pin==1234:
        print("Access granted.")
        break
    else:
        print(f"Incorrect pin. You have {3-attempt} attempts left.")
        pin=int(input("Enter your pin: "))
        if attempt==2:
            print("Access denied. Please try again later.")
            exit()
total_balance = 10000

choice = "0"
while choice != "4":
    print("Welcome to the ATM Simulator!")
    print("1. Check Balance")   
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")   

    
    match choice:
        case "1":
                print(f"Your balance is {total_balance}.")
                
                
        case "2":
                deposit = float(input("Enter the amount to deposit: "))
                if deposit <= 0:
                    print("Invalid amount. Please enter a positive value.")
                    continue
                total_balance += deposit
                print(f"Amount {deposit} deposited successfully.")
                print(f"Your balance is {total_balance}.")
                
        case "3":
                withdraw = float(input("Enter the amount to withdraw: "))
                if withdraw <= total_balance and withdraw > 0:
                    total_balance -= withdraw   
                    print(f"Amount {withdraw} withdrawn successfully.")
                elif withdraw <=0:
                    print("Invalid amount. Please enter a positive value.")
                    continue
                else:
                    print("Insufficient balance.")
                print(f"Your balance is {total_balance}.")
                
        case "4":
                print("Thank you for using our ATM.")
                break
        case _:
                print("Invalid choice. Please enter a number between 1 and 4.")
                



    



    