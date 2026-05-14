import random

print("===== NUMBER GUESSING GAME =====")

# Generate random number
secret_number = random.randint(1, 100)

attempts = 0

while True:
    # User input
    guess = int(input("Guess a number between 1 and 100: "))
    
    attempts += 1

    # Checking the guess
    if guess > secret_number:
        print("Too high!")

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Congratulations! You guessed the correct number.")
        print("Total attempts:", attempts)
        break