#Program No 8

#Hero's Inventory 2.0
#Demonstrates tuples

#create tuple with some items and disply with a for loop
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")
print("Your items: ")
for item in inventory:
    print(item)

input("\n Press the Enter key to continue.")

#get the length of a tuple
print("You have", len(inventory), "items in your possession.")

input("\n Press the enter key to continue.")

#test for membrship with in
if "healing potion" in inventory:
    print("You will live to fight another day.")

#display one item through an index
index = int(input("\nEnter the index number for an item in inventory: "))
print("At index", index ,"is", inventory[index])

#display a slice
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("Enter the Index number to end the slice: "))
print("inventory[",start,":",finish,"] is",end=" ")
print(inventory[start:finish])

input("\nPress the enter key to continue.")

#concatinate two tuples
chest = ("gold","gems")
print("You find a chest. It contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)

input("\n\nPress the Enter key to exit.")
