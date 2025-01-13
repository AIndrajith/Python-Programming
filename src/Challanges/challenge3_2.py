#Flip a coin 100 times
#tells number of head count and tail count

import random

head_count = 0
tail_count = 0
count = 0

while count < 100:
    flip = random.randint(1,2)
    if flip == 1:
        tail_count += 1
    else:
        head_count += 1
    count += 1    

print("\nNumber of Head counts : ",head_count)
print("\nNumber of Tail counts : ",tail_count)

input("\n\nPress the enter key to exit.")