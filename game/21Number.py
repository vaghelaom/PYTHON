# For questions, suggestions, or corrections, contact me at vaghelaom65@gmail.com

# 21 Number game for 2 players

import random

# for toss

firstPerson = input("Enter First Person name: ")
secondPerson = input("Enter Second Person name: ")
print("\nWho gonna take first turn? Have a problem Let's solve it using toss\n")

hort = ["heads", "tails"]
hort1 = ["tails", "heads"]
mainhort = ["heads", "tails"]
rcMain = random.choice(mainhort)
tossForFisrt = 0
tossForSecond = 0

flipCoin = input(f"Who gonna flip coin {firstPerson} or {secondPerson}? Now it's upto you to decide: ")
flipCoin = flipCoin.lower()
if (flipCoin in firstPerson):
    userhort = input(f"{secondPerson} choose heads or tails: ")
    userhort = userhort.lower()
    if (userhort in "heads"):
      print(f"{secondPerson} choose {hort[0]}")
      hort.pop(0)
      print(f"{firstPerson} choose {hort[0]}")
      if (userhort in rcMain):
         print(f"It's {rcMain}")
         print(f"{secondPerson} won")
         tossForSecond = 1
         print("Answer is Generated randomly")
      else:
         print(f"It's {rcMain}")
         print(f"{firstPerson} won")
         tossForFisrt = 1
         print("Answer is Generated randomly")
    elif (userhort in "tails"):
        print(f"{secondPerson} choose {hort1[0]}")
        hort1.pop(0)
        print(f"{firstPerson} choose {hort1[0]}")
        if (userhort in rcMain):
            print(f"It's {rcMain}")
            print(f"{secondPerson} won")
            tossForSecond = 1
            print("Answer is Generated randomly")
        else:
            print(f"It's {rcMain}")
            print(f"{firstPerson} won")
            tossForFisrt = 1
            print("Answer is Generated randomly")
    else:
       print("Invalid input")

elif (flipCoin in secondPerson):
    userhort = input(f"{firstPerson} choose heads or tails: ")
    userhort = userhort.lower()
    if (userhort in "heads"):
      print(f"{firstPerson} choose {hort[0]}")
      hort.pop(0)
      print(f"{secondPerson} choose {hort[0]}")
      if (userhort in rcMain):
         print(f"It's {rcMain}")
         print(f"{firstPerson} won")
         tossForFisrt = 1
         print("Answer is Generated randomly")
      else:
         print(f"It's {rcMain}")
         print(f"{secondPerson} won")
         tossForSecond = 1
         print("Answer is Generated randomly")
    elif (userhort in "tails"):
        print(f"{firstPerson} choose {hort1[0]}")
        hort1.pop(0)
        print(f"{secondPerson} choose {hort1[0]}")
        if (userhort in rcMain):
            print(f"It's {rcMain}")
            print(f"{firstPerson} won")
            tossForFisrt = 1
            print("Answer is Generated randomly")
        else:
            print(f"It's {rcMain}")
            print(f"{secondPerson} won")
            tossForSecond = 1
            print("Answer is Generated randomly")
    else:
       print("Invalid input")

# game logic start from here

firstPersonNumber = 0
secondPersonNumber = 0
mainNumber = 0
AddNumber = 0
secondAddNumber = 0
mainChanceOverFP = 0
mainChanceOverSP = 0
firstPersonChanceOver = 1
secondPersonChanceOver = 1
l = []

# if first person is first

if tossForFisrt == 1 :
   print(f"{firstPerson} you are first")
   while mainNumber <= 21:
        
        if mainNumber > 20:
           print(f"{firstPerson} won")
           break

        firstPersonNumber = int(input(f"{firstPerson} choose 1 or 2 or 3: "))
        mainNumber += firstPersonNumber

        if (firstPersonNumber < 0 or firstPersonNumber > 3) :
           print("Invalid input chance over")
           mainChanceOverFP += firstPersonChanceOver
           mainNumber -= firstPersonNumber
           if mainChanceOverFP == 3:
              print("Game Over")
              break
        else:
           l.append(mainNumber)
           print(l)
         
        if mainNumber > 20:
           print(f"{secondPerson} won")
           break
        secondPersonNumber = int(input(f"{secondPerson} choose 1 or 2 or 3: "))
        mainNumber += secondPersonNumber
        if (secondPersonNumber < 0 or secondPersonNumber > 3) :
           print("Invalid input chance over")
           mainChanceOverSP += secondPersonChanceOver
           mainNumber -= secondPersonNumber
           if mainChanceOverSP == 3:
              print("Game Over")
              break
        else:
           l.append(mainNumber)
           print(l)


# if second person is first

elif tossForSecond == 1 :
   print(f"{secondPerson} you are first")
   while mainNumber <= 21:
        
        if mainNumber > 20:
           print(f"{secondPerson} won")
           break

        secondPersonNumber = int(input(f"{secondPerson} choose 1 or 2 or 3: "))
        mainNumber += secondPersonNumber

        if (secondPersonNumber < 0 or secondPersonNumber > 3) :
           print("Invalid input chance over")
           mainChanceOverSP += secondPersonChanceOver
           mainNumber -= secondPersonNumber
           if mainChanceOverSP == 3:
              print("Game Over")
              break
        else:
           l.append(mainNumber)
           print(l)
         
        if mainNumber > 20:
           print(f"{firstPerson} won")
           break
        
        firstPersonNumber = int(input(f"{firstPerson} choose 1 or 2 or 3: "))
        mainNumber += firstPersonNumber
        if (firstPersonNumber < 0 or firstPersonNumber > 3) :
           print("Invalid input chance over")
           mainChanceOverFP += firstPersonChanceOver
           mainNumber -= firstPersonNumber
           if mainChanceOverFP == 3:
              print("Game Over")
              break
        else:
           l.append(mainNumber)
           print(l)

else:
   print("wrong key press game over start again")