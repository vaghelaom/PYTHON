# For questions, suggestions, or corrections, contact me at vaghelaom65@gmail.com

# number guessing game

from random import *

number = randint(1, 100)
count = 0
while True:
    x = int(input("\nGuess the number between 1 to 100 : "))
    count += 1
    if count == 20:
        print("\nYou have out of chances")
        print("\nThe number was :", number)
        print("\nBetter luck next time\n")
        break
    if x == number:
        print("\nYou won the game. Congratulation")
        print("\nYou guessed it right in", count, "guesses\n")
        break
    elif x<number:
        print("Your guess is TOO LOW")
    elif x>number:
        print("Your guess is TOO HIGH")
    else:
        print("Invalid input")

if count == 5:
    print("\nYou're Genius\n")

