import random

def choose_difficulty():

    print("\nChoose a difficulty level:")
    print("1. Easy Mode (Choose between 1-50, 10 attempts)")
    print("2. Medium Mode ( Choose between 1-100, 7 attempts)")
    print("3. Hard Mode ( Choose between 1-200, 5 attempts)")

    while True:
        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            return 50, 10
        elif choice == "2":
            return 100, 7
        elif choice == "3":
            return 200, 5
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


def play_game():
    max_number, attempts = choose_difficulty()
    secret_number = random.randint(1, max_number)

    print(f"\nI'm thinking of a number between 1 and {max_number}")
    print(f"You have {attempts} attempts to guess it.")

    while attempts > 0:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == secret_number:
            print("🎉 Congratulations! You guessed the number!")
            return

        elif guess < secret_number:
            print("Too low!")

        else:
            print("Too high!")

        attempts -= 1
        print(f"Attempts remaining: {attempts}")

    print(f"\n💀 Game Over! The correct number was {secret_number}.")


def main():
    print("🎮 Welcome to the Number Guessing Game!")

    while True:
        play_game()

        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("Thanks for playing! 👋")
            break


if __name__ == "__main__":
    main()