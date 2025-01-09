#Trust Fund Buddy- Bad
#Demonstrates a logicak error

print(
"""
            Trust Fund Buddy

Total your monthly spending so that your trust fund doesn't run out
(and you're forced to get a real job).

Please enter the requested, monthly costs. Since you're rich, ignore pennies and use only dollar ammounts.

"""
    )

car  = input("Lambogini Tune-Ups: ")
rent = input("Manhattan Appartment: ")
jet  = input("Private Jet Rental: ")
gifts= input("Gifts: ")
food = input("Dinning out: ")
staff= input("Staff(butlers, chef, driver, assistanr): ")
guru = input("Personal Guru And Coach: ")
games= input("Computer Games: ")

total= car + rent + jet + gifts + food + staff + guru +games

print("\nGrand Total: ",total)

input("\n\nPress the enter key to exit.")
