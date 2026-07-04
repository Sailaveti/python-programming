import re

print("===== PASSWORD STRENGTH CHECKER =====")

password = input("Enter your password: ")

# Conditions
length_check = len(password) >= 8
number_check = re.search(r"[0-9]", password)
uppercase_check = re.search(r"[A-Z]", password)
special_check = re.search(r"[@#$%^&*!]", password)

# Checking password strength
if length_check and number_check and uppercase_check and special_check:
    print("Strong Password")
else:
    print("Weak Password")

    print("\nPassword should contain:")
    
    if not length_check:
        print("- At least 8 characters")

    if not number_check:
        print("- At least 1 number")

    if not uppercase_check:
        print("- At least 1 uppercase letter")

    if not special_check:
        print("- At least 1 special character")