#************************************#
#   COMP CLUB Autumn Workshops 2024  #
#    Topic: intro/cont to python     #
#************************************#

def main():
    """
    For each function:
    - provide some themed context
    - run the function, if it returns something, print it in theme
    - leave plenty of comments and a docstring
    """

    ## Some Examples ##

    # Your name
    print("What's your name?")
    name = example_func()

    # The length of your name
    print("How many letters are there in your name?")
    length = name_length(name)
    print(f"{length}'s name has {length} letters")

    ## TODO: add your exersise functions below, be as silly and creative as you want :) ## 

def example_func():
    """prints your name and returns your name
    Returns:
        string: your name
    """
    # TODO: add your name in the double-quotes
    print("Totoro")
    return "Totoro"

def name_length(name):
    """returns the length of a string
    Args:
        name (string): _description_
    Returns:
        int: length of the string
    """
    # TODO: replace me with your code
    return 0

if __name__ == "__main__":
    main()
