import random

SCORE_START = 100
SCORE_PENALTY = 10
SCORE_MIN = 10


def get_difficulty():
    print("\nChoose a difficulty level:")
    print("1. Easy   (1 to 50)")
    print("2. Medium (1 to 100)")
    print("3. Hard   (1 to 200)")
    while True:
        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            return 1, 50
        if choice == "2":
            return 1, 100
        if choice == "3":
            return 1, 200
        print("Invalid choice. Please enter 1, 2, or 3.")


def get_guess(lo, hi):
    while True:
        raw = input(f"Guess a number between {lo} and {hi}: ").strip()
        try:
            guess = int(raw)
        except ValueError:
            print("That is not a whole number. Please try again.")
            continue
        if guess < lo or guess > hi:
            print(f"Your guess must be between {lo} and {hi}.")
            continue
        return guess


def get_score(attempts):
    score = SCORE_START - (attempts - 1) * SCORE_PENALTY
    return max(score, SCORE_MIN)


def praise(attempts):
    if attempts == 1:
        return "Incredible! You found it on the first try!"
    if attempts <= 3:
        return "Excellent guesswork!"
    if attempts <= 6:
        return "Well done!"
    return "You got there in the end!"


def play_round():
    lo, hi = get_difficulty()
    secret = random.randint(lo, hi)
    attempts = 0

    print("\nI am thinking of a number... let's see how fast you find it!")

    while True:
        guess = get_guess(lo, hi)
        attempts += 1
        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            break

    score = get_score(attempts)
    print(f"\n{praise(attempts)} The number was {secret}.")
    print(f"Attempts: {attempts} | Score: {score}")
    return score


def ask_play_again():
    while True:
        answer = input("\nPlay again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer y or n.")


def main():
    print("=" * 40)
    print("       Number Guessing Game")
    print("=" * 40)
    best_score = None

    while True:
        score = play_round()
        if best_score is None or score > best_score:
            best_score = score
            print(f"New best score this session: {best_score}")
        else:
            print(f"Best score this session: {best_score}")

        if not ask_play_again():
            break

    print(f"\nThanks for playing! Your best score was {best_score}.")


if __name__ == "__main__":
    main()
