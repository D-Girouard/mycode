#!/usr/bin/env python3
#this library allows us to generate UUID values.
import uuid
howmany = int(input("how many UUIDs shoud be generated? "))

print("Generating UUIDs...")

# range is required because an int cannot be looped
for rando in range(howmany):
    print( uuid.uuid4() )


