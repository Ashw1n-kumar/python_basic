balance = 10000  # initial balance
amount = int(input("Enter amount to withdraw: "))

if amount <= 0:
    print("Invalid amount!")
elif amount > balance:
    print("Insufficient balance!")
elif amount % 100 != 0:
    print("Amount must be in multiples of 100")
else:
    balance -= amount
    print(f"Withdrawal successful! Remaining balance: ₹{balance}")
