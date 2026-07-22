balance = 500.00

money = float(input("Enter the amount you want to withdraw: R"))


if money <= 0:
    print("Invalid input. You must withdraw more than 'R0'")
    
elif money <= balance:
    remaining = balance - money
    print(f"Withdraw successful! Remaining balance is R{remaining}")

else:
    print("Declined. Insufficiant funds")