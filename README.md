# Number Guessing Game (Python CLI)

A simple command-line number guessing game built with Python. The computer randomly selects a number between 1 and 100, and the player tries to guess it within a limited number of attempts based on the chosen difficulty.

## Features

* Random number generation (1–100)
* Three difficulty levels:

  * Easy (10 attempts)
  * Medium (5 attempts)
  * Hard (3 attempts)
* Hints after each guess (“Too high” / “Too low”)
* Tracks number of attempts
* Win / lose game conditions

## How to Run

1. Make sure Python is installed
2. Run the script:

```bash
python main.py
```

## How It Works

* The player selects a difficulty level
* The program generates a random secret number
* The player guesses until they win or run out of attempts
* The game gives feedback after each guess

## What I Learned

* Using functions
* Loops and conditionals
* User input handling
* Random number generation
* Building a full CLI game
