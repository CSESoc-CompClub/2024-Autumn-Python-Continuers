#************************************#
#   COMP CLUB Autumn Workshops 2024  #
#    Topic: Strings!                 #
#************************************#

# Change the code so that we can read in some text for our 
# first_name, last_name, and numbers, then strings the pieces together a
# and returns the email.

# An example is:
# first_name = "Chihiro"
# last_name = "Ogino"
# numbers = 01
# Email: Chihiro.Ogino01@example.com

def main():
    first_name = input("Your first name: ")
    last_name = input("Your last name: ")
    numbers = input("Some numbers if you want!: ")
    print("Generated Email:")
    print(first_name + '.' + last_name + numbers + '@compclub.org')

#################################################
main()

