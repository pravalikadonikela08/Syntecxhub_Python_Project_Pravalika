# Simple CLI Calculator

# ----- Calculation Functions -----
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


# ----- Calculator Logic -----
def calculate(num1, operator, num2):
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return subtract(num1, num2)
    elif operator == "*":
        return multiply(num1, num2)
    elif operator == "/":
        return divide(num1, num2)
    else:
        return "Invalid operator"


# ----- Menu Function -----
def menu():
    print("\n--- Simple Calculator ---")
    print("1. Perform Calculation")
    print("2. Clear Screen")
    print("3. Exit")


# ----- Main Program -----
while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            num1 = int(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = int(input("Enter second number: "))

            result = calculate(num1, operator, num2)
            print("Result:", result)

        except ValueError:
            print("Invalid input! Please enter numbers only.")

    elif choice == "2":
        print("\nCalculator Cleared\n")

    elif choice == "3":
        print("Exiting calculator. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from the menu.")