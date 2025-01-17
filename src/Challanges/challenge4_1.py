#creating a number sequence 
#as required by user

start_number = int(input("Enter the starting nmber: "))
end_number = int(input("\nEnter the ending number: "))
count = int(input("\nEnter the count do you want: "))

#method 1
#while start_number <= end_number:
#   print(start_number)
#   start_number += count

#method 2
for i in range(start_number,end_number,count):
    print (i, end = " ")


input("\n\nPress the enter key to exit.")    
