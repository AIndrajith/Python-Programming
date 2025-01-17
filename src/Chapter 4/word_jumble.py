# Program No 9

#Word jumble
#
#The computer picks a random word and then "Jumble" it
#The player has guess the original word

import random

#create a sequence of words to choose from
WORDS = ("python","jumble","easy","difficult","answer","xylophone")

#pick one word randomly from the sequence
word = random.choice(WORDS)

#create a variable to use later to see if the guess is correct
correct = word

#create a jumbled veersion of the word
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]
    
#start the game
print(
"""
            Welcome to word Jumble!
    Unscrumble the letters to make a word.
(Press the enter key at the prompt to quit.)            
"""
)
print("The jumble is: ",jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != '':
    print("Sorry, that's not it.")
    guess = input("Your guess: ")

if guess == correct:
    print("thank's it! You guessed it\n")

print("Thanks for plaing.")

input("\n\nPress the enter key to exit.")
