# Password Guess Game

secret_password = "python123"
attempts_left = 3  # Limit number of tries

print("🔐 Welcome to the Password Guess Game!")
print("You have 3 attempts to guess the password.\n")

while attempts_left > 0:  # condition to keep looping
    guess = input("Enter password: ")

    if guess == secret_password:
        print("✅ Access granted! Welcome!")
        break  # Exit the loop immediately if correct
    else:
        attempts_left -= 1
        print(f"❌ Wrong password. Attempts left: {attempts_left}")

        if attempts_left == 0:
            print("⛔ Too many wrong tries. Access denied!")
