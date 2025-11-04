# NumberGuessing_Advanced.py
# ------------------------------------------------------------
# 🧠 Author: Nihal Patel
# 🎯 Project: Advanced Number Guessing Game
# 💻 Language: Python 3
# ------------------------------------------------------------
# Features:
# - Dynamic difficulty levels (Easy / Medium / Hard)
# - Score and attempt tracking
# - Input validation and exception handling
# - Random number generation within user-defined range
# - Replay option
# ------------------------------------------------------------

from random import randint
from time import sleep

def get_valid_input(prompt: str, low: int, high: int) -> int:
    """Safely get a valid integer input within a given range."""
    while True:
        try:
            guess = int(input(prompt))
            if low <= guess <= high:
                return guess
            print(f"⚠️  Please enter a number between {low} and {high}.")
        except ValueError:
            print("❌ Invalid input! Enter a valid integer.")


def choose_difficulty() -> tuple[int, int, int]:
    """Allow user to choose difficulty and return (low, high, attempts)."""
    print("\n🎮 Choose your difficulty level:")
    print("1. Easy (1–10, 5 attempts)")
    print("2. Medium (1–50, 7 attempts)")
    print("3. Hard (1–100, 10 attempts)")

    choice = input("Enter choice (1/2/3): ").strip()
    if choice == "1":
        return 1, 10, 5
    elif choice == "2":
        return 1, 50, 7
    elif choice == "3":
        return 1, 100, 10
    else:
        print("⚠️  Invalid choice! Defaulting to Medium difficulty.")
        return 1, 50, 7


def play_game():
    """Main game logic."""
    print("\n🎯 Welcome to the Advanced Number Guessing Game!")
    low, high, attempts = choose_difficulty()
    secret_number = randint(low, high)
    score = 0

    print(f"\nI'm thinking of a number between {low} and {high}.")
    print(f"You have {attempts} attempts. Let's begin!\n")

    for attempt in range(1, attempts + 1):
        guess = get_valid_input(f"Attempt {attempt}/{attempts} → Guess: ", low, high)

        if guess < secret_number:
            print("⬆️  Too low! Try a higher number.")
        elif guess > secret_number:
            print("⬇️  Too high! Try a lower number.")
        else:
            print(f"\n✅ Correct! You guessed the number in {attempt} attempts.")
            score = (attempts - attempt + 1) * 10
            print(f"🏆 Your score: {score}\n")
            break
    else:
        print(f"\n❌ Out of attempts! The correct number was {secret_number}.\n")

    return score


def main():
    """Game entry point with replay system."""
    total_score = 0

    while True:
        total_score += play_game()
        again = input("🔁 Do you want to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("\n💥 Thanks for playing!")
            print(f"🎖️ Total Score: {total_score}")
            sleep(1)
            print("Goodbye 👋")
            break


if __name__ == "__main__":
    main()