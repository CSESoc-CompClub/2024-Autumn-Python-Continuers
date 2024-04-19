
#************************************#
#   COMP CLUB Autumn Workshops 2024  #
#    Topic: Printing!                #
#************************************#

# DO NOT TOUCH
def main():
    print("-==Printing 1==-")
    print_hello_world()
    
    print("\n\n-==Printing 2==-")
    print_maths()

    print("\n\n-==Printing 3==-")
    print_facts()

    print("\n\n-==Printing 4==-")
    print_multiple()


# [Printing 1] ################################################################
#
# Welcome to the COMP CLUB Autumn workshop! As is tradition, let us say hello to the world!
#
# Task: print out the phrase
#    Hello world!
#

def print_hello_world():
    print("To do!")
    #<--Your code here-->#

# [Printing 2] ################################################################
#
# To prepare us for the future, let's do some basic maths.
# We can use python as a calculator!
#
# Task: Print out the value of the following:
#   a) Add the numbers 123 and 456 (Done for you!)
#   b) Add the numbers 4373000 and 9221250
#   c) Subtract 2165625 from 4375000
#   d) Multiply 42537 by 29530
#   e) Divide 52305765 by 4237
#   f) Integer part of 520537 divided by 500
#   g) EXTRA: There is another maths operator '%', see if you can figure
#       out what it does!
#       HINT: try print(x % 4), for x = 0, 1, ..., 10.

def print_maths():
    print("TODO")
    #<--Your code here-->#

# [Printing 3] ################################################################
#
# One cool thing we can do is print the value of a variable.
# Set values of the variables, and the print function will 
# fill out the information for you!
def print_facts():
    print("TODO")
    my_name = "your_name_here"
    my_school = "your_school_here"
    my_age = 0 #Your age here, as a number
    my_hobby = "your_hobby_Here"
    print("Hi! My name is", my_name, "I am", my_age, "years old, and I go to school at", my_school,"I often enjoy", my_hobby)

    # Now, try to write one of these print statements yourself!
    # Fill in the spaces in the print statement to make the equation true.
    #
    x = 2
    y = 6
    z = 12

    # print(___, "times", ___, "equals", ___)
    

# [Printing 4] ################################################################
#
# One more thing. Sometimes, we need to print a lot of things over many lines.
# One example is ascii art!

# We can do this by using three quotation marks at the beginning and 
# end of what we want to print
#
# Here is an example:
def print_multiple():
    print(
        """
              |\\
              | \\
              |  \\
              |   )
              |  /  
             _|.'
           .' |
          /   |_.
         |  .'|  '.
          \ * |   /
           '._|_.'
              |
            * |
            '.'
        """
    )

# Head on over to https://www.asciiart.eu/ and try this for yourself!
    print("-|My ASCII art|-")
    print(
        """
        """
    )

###########################################################################
main()
