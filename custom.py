message = 'Your grade letter is  '

# wrap connection in a float() to accept decimals as numbers
score = float(input("What is your score number?"))
except  

# if input >= 90
if score >= 90:
    message = message + 'A'

elif score >= 80:
    message = message + 'B'

elif score >= 70:
    message = message + 'C'

elif score >= 60:
    message = message + 'D'

elif score >= 0:
    message = message + 'F'

else:
    print("ENTER A VALID SCORE")

print(message)    
                                               
