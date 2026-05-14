print("===== SIMPLE CLI CALCULATOR =====")

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Showing operations
print("\nChoose Operation")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Power (^)")

choice = input("Enter choice (1-6): ")

# Performing operations using if-elif
if choice == "1":
    result = num1 + num2
    print("Result =", result)

elif choice == "2":
    result = num1 - num2
    print("Result =", result)

elif choice == "3":
    result = num1 * num2
    print("Result =", result)

elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print("Result =", result)
    else:
        print("Error: Division by zero is not allowed")

elif choice == "5":
    result = num1 % num2
    print("Result =", result)

elif choice == "6":
    result = num1 ** num2
    print("Result =", result)

else:
    print("Invalid choice")