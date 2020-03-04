#!/usr/bin/env python3

message = 'The movie is a bout to begin, we recommend '

# wrap connection in a float() to accept decimals as numbers
connection = float(input("What is your connection speed in Mbps?"))

# if input >= 25
if connection >= 25:
    message = message + 'setting video to 4k.'

elif connection >= 5:
    message = message + 'setting video to 1080p.'

else:
    message = message + 'finding another access network.'

print(message)
