import random

def choose_difficulty():
    print("Choose difficulty:")
    print("1) Easy  (1-10, 6 attempts)")
    print("2) Normal(1-50, 7 attempts)")
    print("3) Hard  (1-100, 8 attempts)")
    choice = input("Enter 1, 2 or 3: ").strip()
    if choice == "1":
        return 1, 10, 6
    elif choice == "2":
        return 1, 50, 7
    else:
        # default to hard if input invalid or "3"
        return 1, 100, 8

def play_round():
    low, high, attempts_left = choose_difficulty()
    secret = random.randint(low, high)
    print(f"\nI have chosen a number between {low} and {high}.")
    print(f"You have {attempts_left} attempts. Good luck!\n")

    while attempts_left > 0:
        guess_str = input(f"Enter your guess ({attempts_left} attempts left): ").strip()
        # input validation
        if not guess_str.isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(guess_str)

        if guess < low or guess > high:
            print(f"Your guess is outside the range {low}-{high}. Try again.")
            continue

        # conditional logic: if / elif / else
        if guess == secret:
            print(f"🎉 Correct! The number was {secret}. You win!")
            return True
        elif guess < secret:
            attempts_left -= 1
            print("Too low!")
        else:  # guess > secret
            attempts_left -= 1
            print("Too high!")

        if attempts_left == 0:
            print(f"\n😞 You've run out of attempts. The number was {secret}.")
            return False

def main():
    print("Welcome to Guess the Number!\n")
    while True:
        play_round()
        again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing — bye!")
            break
        print()

if __name__ == "__main__":
    main()
