# PROG 4: Number Guessing Game

# Write The Code Here
import random

number = random.randint(1, 100)
chances = 10

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100. You have 10 chances to guess it.")

while chances > 0:

    guess = input("\nEnter your guess (between 1 and 100): ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    if guess == number:
        print("Congratulations! You guessed the number correctly:", number)
        break

    elif guess < number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")

    chances -= 1
    print("Chances left:", chances)

if chances == 0:
    print("You lost! The correct number was:", number)