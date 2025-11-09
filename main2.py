import random

# List of choices
choices = ["rock", "paper", "scissors"]

while True:
    # Get user input
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
    
    if user_choice == "quit":
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    # Computer choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Decide winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")
    
    print("-" * 30)