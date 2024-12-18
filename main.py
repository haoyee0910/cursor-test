import random

def guess_the_number():
    # Generate a random number between 1 and 50
    secret_number = random.randint(1, 50)
    attempts = 0
    max_attempts = 20

    print("Welcome to Guess the Number!")
    print(f"I'm thinking of a number between 1 and 50. You have {max_attempts} attempts to guess it.")
    base_port = 8000 

    while attempts < max_attempts:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess
            if guess < secret_number:
                print("Too low! Try a bigger number pls.")
            elif guess > secret_number:
                print("Too high! Try a smaller number pls.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                return

            # Inform the player of remaining attempts
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"You have {remaining} attempts left.")
            else:
                print(f"Game over! The number was {secret_number}.")

        except ValueError:
            print("Please enter a valid number.")

    print(f"Sorry, you've run out of attempts already. The number was {secret_number}.")

# Run the game
if __name__ == "__main__":
    guess_the_number()
