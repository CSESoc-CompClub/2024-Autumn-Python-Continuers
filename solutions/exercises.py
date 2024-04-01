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
    print()

    # The length of your name
    print("How many letters are there in your name?")
    length = name_length(name)
    print(f"{length}'s name has {length} letters\n")

    # Catbus Capacity
    print("Mei is lost! How much ground have we covered?")
    test(10, ground_covered([5, 2, 3]))

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

def ground_covered(distances):
    """returns the ground covered
    Args:
        distances (int[]): ground covered by each character
    Returns:
        int: total ground covered
    """
    # TODO: add your code here
    return 0

def test(expected, actual):
    """
    Helper for testing, useful for computational exersises
    """
    if expected != actual:
        print("\x1b[31m+----------- Test Failed -----------+\x1b[89m")
        print(f"expected {expected} but received {actual}")
    else:
        print("\x1b[32m+----------- Test Passed -----------+\x1b[89m")
    print("\x1b[0m\x1b[0m\r", end="")

if __name__ == "__main__":
    main()
