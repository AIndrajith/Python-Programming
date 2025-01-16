# Program No 7

#Hero's Inventory
#Demonstrates tuples creation

#create an empty tuple 
inventory = ()

#treat the tuple as a location
if not inventory:
    print("You are empty-handed.")

input("\nPress the enter key to Continue.")

#create a tuple with some items    
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")

#print the tuple
print("\nThe tuple inventory is: ")
print(inventory)

#print each element in the tuple
print("\nYour items:")
for item in inventory:
    print(item)

input("\n\nPress the enter key to exit.")    
