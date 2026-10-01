balance=10000.0
print("..............Welcome to Bank ATM...............")
while True:
    print(" -----ATM Menu-----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice=input("Enter your choice (1-4): ")

    match choice:
        case '1':
            print("Your current balance is :Rs. {balance}")

        case '2':
            amount =float (input("Enter amount to deposit : Rs. ")) 
            if amount>0:
                balance +=amount
                print(f"Rs. {amount} deposited sucessfully  ")   
                print(f"Updated balance :Rs.{balance}")
            else:
                print("Invalid amount")

        case '3':
            amount =float (input("Enter amount to withdraw : Rs. "))  
            if amount<=0:
                print("Invalid amount!")
            elif amount>balance:
                print("Insufficient balance!")
                print("Your current balance is :Rs. {balance}")
            else:
                balance-=amount
                print(f"Rs. {amount} withdrawn sucessfully")
                print(f"Remaining balance:Rs.{balance}")

        case '4':
            print("Thank you for using Bank ATM GoodBye!")  
            break

        case _:
            print("Invalid choice! Please select 1-4 only.")      



