#print the string backword

message = input("Enter the message: ")
length = len(message)

new_message= ""

while length > 0:
    new_message += message[length-1]
    length -= 1

print("\n Your message in backword: ", new_message)

input("\n\nPress the enter key to exit.")