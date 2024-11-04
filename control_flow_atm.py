def atm_program():
    # Initial balance and PIN
    balance = 15000.00
    pin = '2508'
    attempts = 0

    # PIN verification loop
    while attempts < 3:
        user_pin = input("Please enter your ATM PIN: ")
        if user_pin == pin:
            print("Access granted.")
            break
        else:
            attempts += 1
            print(f"Incorrect PIN. You have {3 - attempts} attempts left.")
    else:
        print("Too many incorrect attempts. Access blocked.")
        return  # Exit the program if PIN is incorrect

    # Main menu loop
    while True:
        print("\n--- Main Menu ---")
        print("1. Check Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        # Check Balance
        if choice == '1':
            print(f"Your balance is: ${balance:.2f}")
        
        # Deposit Funds
        elif choice == '2':
            amount = input("Enter the amount to deposit: ")
            if amount.isdigit() and float(amount) > 0:
                balance += float(amount)
                print(f"Deposited ${amount}. New balance is: ${balance:.2f}")
            else:
                print("Invalid input. Please enter a positive number.")

        # Withdraw Funds
        elif choice == '3':
            amount = input("Enter the amount to withdraw: ")
            if amount.isdigit() and float(amount) > 0:
                amount = float(amount)
                if amount <= balance:
                    balance -= amount
                    print(f"Withdrew ${amount}. New balance is: ${balance:.2f}")
                else:
                    print("Insufficient funds.")
            else:
                print("Invalid input. Please enter a positive number.")

        # Change PIN
        elif choice == '4':
            new_pin = input("Enter your new 4-digit PIN: ")
            if new_pin.isdigit() and len(new_pin) == 4 and new_pin != pin:
                pin = new_pin
                print("Your PIN has been successfully changed.")
            else:
                print("Invalid PIN. It must be a different 4-digit number.")

        # Exit the Program
        elif choice == '5':
            print("Exiting... Thank you for using the ATM.")
            break
        
        # Invalid Choice
        else:
            print("Invalid choice. Please select a valid option.")

# Run the ATM program
atm_program()
