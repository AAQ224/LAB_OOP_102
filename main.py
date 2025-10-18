from bank_account import BankAccount

account1 = BankAccount("Abdulrahman", 500)
account2 = BankAccount("Abdulaziz")
account3 = BankAccount("Omar", 1000)

for acc in [account1, account2, account3]:
    print(f"Account Holder: {acc.get_account_holder()} - Balance: {acc.get_balance()}")

print("\n(Transactions)")
print("\n(Abdulrahman's Account)")

try:
    print("Depositing 200")
    account1.deposit(200)
    print("New Balance:", account1.get_balance(), "SR")
except Exception as e:
    print("Error:", e)

try:
    print("Withdrawing 100")
    account1.withdraw(100)
    print("New Balance:", account1.get_balance(), "SR")
except Exception as e:
    print("Error:", e)

try:
    print("Withdrawing 1000")
    account1.withdraw(1000)
    
except Exception as e:
    print("Error:", e)


print("\n(Abdulaziz's Account)")
try:
    print("Depositing 500")
    account2.deposit(500)
    print("New Balance:", account2.get_balance(), "SR")
except Exception as e:
    print("Error:", e)

try:
    print("Withdrawing 150")
    account2.withdraw(150)
    print("New Balance:", account2.get_balance(), "SR")
except Exception as e:
    print("Error:", e)


print("\n(Omar's Account)")
try:
    print("Depositing -300")
    account3.deposit(-300)
    print("New Balance:", account3.get_balance(), "SR")
except Exception as e:
    print("Error:", e)

try:
    print("Withdrawing 800")
    account3.withdraw(800)
    print("New Balance:", account3.get_balance(), "SR")
except Exception as e:
    print("Error:", e)


print("\n(Final Balances)")
for acc in [account1, account2, account3]:
    print(f"{acc.get_account_holder()}: {acc.get_balance()} SR")

