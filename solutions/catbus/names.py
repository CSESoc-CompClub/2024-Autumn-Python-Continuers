"""Read a list of names from the player.

This is your second task of the project."""

def input_name_list():
    """Prompt the user for a number, and then read that many names."""
    #<SOLUTION>
    number = int(input('How many names? '))
    names = []
    for i in range(1, number + 1):
        names.append(input(f'{i}: '))
    return names
    #</SOLUTION>