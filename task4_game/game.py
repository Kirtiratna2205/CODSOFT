import random

def play_game():
    user_score = 0
    computer_score = 0

    choices = ["rock", "paper", "scissors"]

    print("===== ROCK PAPER SCISSORS GAME =====")

    while True:
        print("\nChoose one:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

        if user_choice not in choices:
            print("❌ Invalid choice! Please try again.")
            continue

        computer_choice = random.choice(choices)

        print("\nYour choice     :", user_choice)
        print("Computer choice :", computer_choice)

        # Game Logic
        if user_choice == computer_choice:
            print("Result: It's a Tie! 🤝")

        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            print("Result: You Win! 🎉")
            user_score += 1

        else:
            print("Result: You Lose! 😢")
            computer_score += 1

        # Score Display
        print("\nScoreboard")
        print("You      :", user_score)
        print("Computer :", computer_score)

        # Play again option
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("\nThanks for playing Rock-Paper-Scissors! 👋")
            break


# Run the game
play_game()
