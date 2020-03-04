#!/usr/bin/env python3

thisround = 0
while(True):
    print('what is the IPv4 address use to broadcast? ')
    answer = input()
    thisround = thisround + 1
    if (answer == '255.255.255.255'):
        print('Correct!')
        break
    elif (thisround ==3):
        print('sorry, the answer was 255.255.255.255')
        break
    else:
        print('sorry, try again.')

