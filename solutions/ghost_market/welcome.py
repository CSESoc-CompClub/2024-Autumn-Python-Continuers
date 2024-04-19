"""
Open your stall with a welcome message,
and get your customer's name!

This is your first task of the project.
"""


def welcome():
    """Print a warming welcome message!"""
    # <Solution>
    print(f"Opening for the night! Welcome, welcome!\n")
    # </Solution>
    pass


def get_next_customer() -> str:
    """
    Prompt the customer for their name, and return it

    HINT: Use the `input` function
    """
    # <Solution>
    return input("Enter your name: ")
    # </Solution>
    pass


def display_catalogue():
    """
    Display every item in the catalogue.

    HINT: Use the `CATALOGUE` dictionary from `constants.py`
    HINT: Use a `for in` loop (e.g. `for category in CATALOGUE`)
    HINT: For some prettier formatting, use tabs in your print statements (e.g. `print("\t" + ...)`)
    """
    # <Solution>
    print(f"Here's what we have on the catalogue tonight: \n")
    #... print the dictionary, this is up to students
    # </Solution>
    pass
