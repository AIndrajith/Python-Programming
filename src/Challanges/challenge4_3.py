#Word jumble 2.0
#
#The Computer picks a ramdom word and then "Jumble" it
#The Player has guess the original word
#If player got stuck he can see a hint 

import random

#create a sequence of words to choose from
WORDS = ("python","ship","easy","difficult","answer","pineapple")

#create a sequence of hints related to words
HINTS = ("it's aprogramming language","That can be goin on the water","its similer to no difficult","meaning like hard","Any question have this","kind of a fruit")

#pick the word position from the sequence 
w_position = random.randrange(len(WORDS))

#pick the word and hint related to the word
word = WORDS[w_position]
hint = HINTS[w_position]

#declare a variable for scoring part
score = 0

#create a variable to use later to see if the guess is correct
correct = word

#create a jumbled version of the word
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]

#start game
print(
"""
            Welcome to word Jumble!
    Unscrumble the letters to make a word.
(Press the enter key at the prompt to quit.)            
"""
)
print("The jumble is: ",jumble)

guess = input("\nYour guess(If you want a hint type'hint'): ")
while guess != correct and guess != "":
    if guess == "hint":
        print("\nHint: ",hint)
        guess = input("\nNow you can guess it: ")
        score += 1
        continue
    else:
        print("Sorry,that's not it.")
        guess = input("\nYour guess(If you want a hint type'hint'): ")

if score == 0:
    print("That's it!You guessed it and your got 100 points\n")
else:
    print("That's it! now you guessed it and you go 70 points because you got a hint\n")    

input("\n\nPress the enter key to exit.")    