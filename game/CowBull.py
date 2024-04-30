# For questions, suggestions, or corrections, contact me at vaghelaom65@gmail.com

# CowBull Game

import random

def generate_unique_random_number():
    digits = list(range(10))
    random.shuffle(digits)
    # Ensure the first digit is not 0 to maintain 4-digit number
    if digits[0] == 0:
        digits[0], digits[1] = digits[1], digits[0] 
    return ''.join(map(str, digits[:4]))

number = str(generate_unique_random_number())
attemps = 0

print("\n\nREMEMBER : - 4 DIGIT NUMBER ONLY WITH NO REPEATED DIGITS\n\n")

while True:
# Get user input
    guess = input("Guess a 4-digit number: ")
    attemps += 1
    bulls = 0
    cows = 0

# Check the user's guess


    for i in range(4):
        if guess[i] == number[i]:
            bulls += 1

        elif guess[i] in number:
            cows += 1
    print("Bulls:", bulls)
    print("Cows:", cows)
    if bulls == 4:
        print("Congratulations! You guessed the number correctly.")
        print("The number was", number)
        break
    elif attemps == 20:
        print("Sorry, you ran out of guesses. The number was", number)
        break

if(attemps<5):
    print("You're Gineous!")
    
print("You guessed the number in", attemps, "attempts.")