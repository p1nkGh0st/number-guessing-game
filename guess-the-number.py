import random

# 1. Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# 2. Initialize the variable to store the number of attempts
attempts = 0

# 3. Infinite loop until the correct number is guessed
while True:
    try:
        user_input = int(input("Guess the number 1 ~ 10: "))
    except ValueError:
        print("NUMBERS ONLY! Try again.")
        continue  # Catch non-integer inputs and restart the loop

    attempts += 1

    # Check if the user's input matches the secret number
    if user_input == secret_number:
        print(f"GG! You beat the game in {attempts} tries!")
        break

    elif user_input < secret_number:
        print("TOO LOW! Pump it up!")

    else:
        print("TOO HIGH! Bring it down!")
