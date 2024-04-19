
#************************************#
#   COMP CLUB Autumn Workshops 2024  #
#    Topic: Variables!               #
#************************************#

# Write a program that determines how many bowls of ramen 
# a restaurant can make from the given sheets of seaweed. 
# A bowl of ramen must have 3 sheets of seaweed, no more, no less!

# Hint: Do you remember how to get a whole number while dividing?

def main():
    seaweed = float(input("How many sheets of seaweed: "))
    print("The number of ramen: ", int(seaweed / 3))

main()