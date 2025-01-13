#Modified Guess My Number

import random

print("\tWelcome to 'Guess My Number'")
print("\nT'm thinking of a number between 1 and 100")
print("Try ti guess it in as few attempts as possible.\n")

#set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

while tries != 10:
    if guess == the_number:
        break
    elif guess > the_number:
        print("Lower...")
    else:
        print("Higher...")

    guess = int(input("Take a guess: "))
    tries += 1

if tries == 10:
    print("You exeed your tries count")
    print("The number is: ",the_number)
    print("Better luck next Time..Try Again")
else:
    print("You guessed it! The number was", the_number)
    print("And it only took you", tries, "tries!\n")

input("\n\nPress the enter key to exit.")
