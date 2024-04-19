#************************************#
#   COMP CLUB Autumn Workshops 2024  #
#    Topic: if/else!                 #
#************************************#
import random

def main():
    number = random.randint(1,20)
    n = int(input("Your guess: "))
    while(n != number):  
        if (number < n):
            print("Too high!")
        elif (number > n):
            print("Too low!")
            
        n = int(input("Your guess: "))


    print("You got it! The number was", number)

#################################################
main()
