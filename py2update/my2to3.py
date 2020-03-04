#!/usr/bin/env python3
thisround = 0      # integer round initiated to 0
while(True):       # sets up an infinite loop condition
    print('What is the IPv4 address used to broadcast on the local network? ')
    answer = input()    #print answer collected from user
    thisround = thisround + 1    #increase the round counter
    if (answer == '255.255.255.255'):    #logic to check if user gave correct answer
        print('Correct!')
        break
    elif (thisround ==3):    #logic to ensure round has no yet reached 3
        print('Sorry, the answer was 255.255.255.255')
        break
    else:
        print('Sorry, Try again!')

