# For questions, suggestions, or corrections, contact me at vaghelaom65@gmail.com

# word guessing game

print('''
            NOTE : - After every 5 attempts you will be asked if you want to guess the word or not till 20 attempts.
                     If you guess the word wrong , game is over. 
''')

import random

attemps = 0
win = 0

# Open a file and read Word into a list
with open("Word.txt", "r") as file:
    Word = file.read().split()

# Choose a random word from the list
random_word = random.choice(Word)

while True:

    attemps = attemps + 1
    if attemps == 21:
        print(f"Sorry! your 20 chance is over. The word was {random_word}")
        break

    userInput = input("Guess a character: ")

    if userInput in random_word:
        x = random_word.index(userInput) + 1
        print(f"----- > {userInput} is at position {x}")
    else:
        print(f"{userInput} is not in the word")

    if attemps == 5 or attemps == 10 or attemps == 15 or attemps == 20:
        lastAttemp = input("Are you interested to guess the word? (yes/no) : ")
        lastAttemp = lastAttemp.lower()
        if lastAttemp == "yes" or lastAttemp == "y" or lastAttemp == "ye":
            wordInput = input("Guess the word: ")
            if wordInput == random_word:
                print(f"Congratulation! You guessed the word correctly. The word was {random_word}")
                win = 1
                break
            else:
                print(f"Sorry! You guessed the word incorrectly. The word was {random_word}")
                break
        else:
            continue

if win == 1 and attemps <= 20:
    print(f"You guessed the word in {attemps} attempts")
if attemps == 5 and win == 1:
    print("you're a expert in word guessing game.")