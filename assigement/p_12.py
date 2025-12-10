#Day 12 - Exception Handling
# ------------------------------------------
# 1. Division by Zero Handling
# ------------------------------------------
print("------ Division Handling ------")
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid integers!")
else:
    print(f"Result: {result}")
finally:
    print("Division operation completed.\n")


# ------------------------------------------
# 2. Invalid Input Handling
# ------------------------------------------
print("------ Input Validation Example ------")
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
except ValueError as ve:
    print("Invalid input:", ve)
else:
    print(f"Your age is {age}\n")


# ------------------------------------------
# 3. Custom Exception Example
# ------------------------------------------
print("------ Custom Exception Example ------")
class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Custom Error: Number cannot be negative!")
except NegativeNumberError as ne:
    print(ne)
except ValueError:
    print("Please enter a valid integer!")
else:
    print(f"You entered: {num}\n")


# ------------------------------------------
# 4. ATM/Login Simulation
# ------------------------------------------
print("------ ATM/Login Simulation ------")
USER_CREDENTIALS = {"username": "user123", "pin": 1234}
balance = 5000

try:
    username = input("Enter username: ")
    pin = int(input("Enter 4-digit PIN: "))

    if username != USER_CREDENTIALS["username"] or pin != USER_CREDENTIALS["pin"]:
        raise ValueError("Invalid username or PIN!")

except ValueError as ve:
    print("Login Failed:", ve)
else:
    print(f"Welcome {username}!")
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print(f"Your balance: ${balance}")
            elif choice == 2:
                amount = float(input("Enter amount to withdraw: "))
                if amount > balance:
                    raise ValueError("Insufficient balance!")
                balance -= amount
                print(f"${amount} withdrawn. Remaining balance: ${balance}")
            elif choice == 3:
                amount = float(input("Enter amount to deposit: "))
                if amount < 0:
                    raise ValueError("Cannot deposit negative amount!")
                balance += amount
                print(f"${amount} deposited. New balance: ${balance}")
            elif choice == 4:
                print("Thank you for using ATM. Goodbye!")
                break
            else:
                print("Invalid option! Choose 1-4.")
        except ValueError as ve:
            print("Error:", ve)
        except Exception as e:
            print("Unexpected Error:", e)
