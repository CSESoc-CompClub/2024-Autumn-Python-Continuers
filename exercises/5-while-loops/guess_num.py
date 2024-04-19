# Write a program that asks the user to input a guess, 
# UNTIL their guess matches the 'number' variable.
# You should also tell the user if their input was too high or too low.

# Hint: Check how the value of 'number' compares to their input 'n'

import random
#####################################################################
def main():
    number = random.randint(1,20)
    n = int(input("Your guess: "))

    # TODO: Add your code here

    print(f'Yay! the number was {number}')

#####################################################################
main()
