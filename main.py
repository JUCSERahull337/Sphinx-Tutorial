
"""
Importing modules
"""

import random

random_number= random.randint(1,101)
"""
    generating random number from 1 to 100 
"""
print(random_number) # Print the random number
c=0 # count the number of guess
guess=10 #number of guess

while(guess != random_number):

    guess = int(input("Enter your guessed int number: "))

    if(guess>random_number):
        print("Higher")
    elif(guess<random_number):
        print("Lower")
    else:
        print("You guessed it right!!!")
    c=c+1

print("You have taken",str(c),"steps to guess the number")