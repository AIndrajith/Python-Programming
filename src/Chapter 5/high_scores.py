#Program no 2

#High scores
#Demonstrates list methods

scores = []

choice = None

while choice != "0":
    print(
    """
        High Scores

        0 - Exit
        1 - Show Scores
        2 - Add a score
        3 - Delete a Score
        4 - Sort Scores
    """
    )

    choice = input("choice: ")
    print()

#exit
    if choice =="0":
        print("Good-bye.")

#list high-score table
    elif choice == "1":
        print("High Scores")
        for score in scores:
            print(score)        

#add a score
    elif choice == "2":
        score = int(input("What score dod you get?: "))
        scores.append(score)    

#remove a score
    elif choice == "3":
        score = int(input("Remove which score?: "))
        if score in scores:
            scores.remove(score)
        else:
            print(score,"isn't the high scores list.")
            
                        
#sort score
    elif choice == "4":
        scores.sort(reverse=True)
#        for score in scores:
#            print(score) 

# some unknown choice
    else:
        print("Sorry, but", choice, "isn't a valid choice.") 


print("""
                    There are some List methods in this table

__________________________________________________________________________________
|    Method           |   Description                                             |
|---------------------|-----------------------------------------------------------|    
|    append(value)    |   Adds 'value' to end of a list                           |
|    sort()           |   Sorts the elements, smallest value first. Oprtionally,  |
|                     |   you can pass a Boolean value to the parameter 'reverse'.|
|                     |   If you pass 'True', the list will be sorted with the    |
|                     |   Largest value first                                     |
|    reverse()        |   Reverse the order of the list                           |
|    count(value)     |   Returns the number of occurrences of 'value'            |
|    index(value)     |   Returns the first position number of where 'value'      |
|                     |   occurs                                                  |
|    insert(i,value)  |   insert 'value' at position 'i'                          |
|    pop([i])         |   Returns value at position 'i' and removes value from    |
|                     |   the list. Providing the position number 'i' is optional,|
|                     |   Without it. the last element in the list is removed and |
|                     |   returned.                                               |
|    remove(value)    |   Removes the first occurrence of 'value' from the list   |
|_____________________|___________________________________________________________|

""")

input("\n\nPress the enter key to exit.")  