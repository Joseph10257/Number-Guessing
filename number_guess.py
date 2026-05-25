import random as rnd  # random number generator

while True:  # game replay loop

    guess = 0
    guess_attempts = 0  # number of guesses made

    print("Welcome to the Number Guessing Game"
          "\nI'm thinking of a number from 1-100\n")

    def difficulty():
        level = input("""Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
Enter your choice: """).lower()

        if level in ["1", "easy", "e"]:
            return 10
        elif level in ["2", "medium", "m"]:
            return 5
        elif level in ["3", "hard", "h"]:
            return 3

        print("Invalid input. Please choose a valid difficulty level.")
        return difficulty()

    attempts = difficulty()
    number = rnd.randint(1, 100)  # secret number

    while guess != number and guess_attempts < attempts:
        guess = int(input("Make your guess: "))
        guess_attempts += 1

        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"You got it! The answer was {number}. You guessed it in {guess_attempts} attempts.")

    if guess_attempts >= attempts and guess != number:
        print(f"Game over! The number was {number}.")

    play_again = input("\nPlay again? (y/n): ").lower().strip()
    if play_again != "y":
        print("Thanks for playing!")
        break
