import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

while True:
    user = input("\nEnter rock, paper, or scissors (or 'quit' to stop): ").lower()
    
    if user == "quit":
        print("\nFinal Score:")
        print("You:", user_score)
        print("Computer:", computer_score)
        break

    if user not in choices:
        print("Invalid input!")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1