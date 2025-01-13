#Guess my number by Computer
#
#The player picks a random number between 1 and 100
#The computer tries to guess it and player lets the 
#computer know if the guess is too high, too low
#or right on the money

#inport random
import random

print("\tWelcome to 'Guess My Number by the Computer'")
print("\nThink a number between 1 and 100")
print("I'm try to guess that number in few attempts as possible")

#set the initial values
num1 = 1
numm2= 10
tries = 1

the_number = ""
guess = random.randint(num1,numm2)

print("\nTell me if my guess is greater than your number 'L'")
print("\nTell me if my guess is Less than your number 'H'")
print("\n or if i'm correct type 'Done'")

#guessing the loop
while not the_number:
    the_number = input("\nIf you choose a number then type Y : ")

print(guess)

if the_number == "Y":
    the_number = input("L or H or Done:")
    while the_number != "Done":
        if the_number == "L":
            num2 = guess
            guess = random.randint(num1,num2)
            print(guess)
        elif the_number == "H":
            num1 = guess
            guess = random.randint(num1,num2)
            print(guess)
        else:
            input("Enter the Correct word or Letter: ")
        tries += 1
    if the_number == "Done":
        print("I guess your number in ",tries, "Tries")
        print("And your number is: ",guess)        

else:
    print("\nChoose a number and type Y if you're ready.")  
    

input("\n\nPress the enter key to exit.")