#Trust Fund Buddy- Good
#Demonstrates type Conversion

print(
"""
            Trust Fund Buddy

Totals your monthly spending so that your trust fund doesn't run out
(and you're forced to get a real job).

Please enter the requested, monthly costs. Since you're rich, ignore pennies and use only dollar ammounts.

"""
    )

car  = input("Lambogini Tune-Ups: ")
car  = int(car)
rent = int(input("Manhattan Appartment: "))
jet  = int(input("Private Jet Rental: "))
gifts= int(input("Gifts: "))
food = int(input("Dinning out: "))
staff= int(input("Staff(butlers, chef, driver, assistanr): "))
guru = int(input("Personal Guru And Coach: "))
games= int(input("Computer Games: "))

total= car + rent + jet + gifts + food + staff + guru +games

print("\nGrand Total: ",total)

input("\n\nPress the enter key to exit.")
