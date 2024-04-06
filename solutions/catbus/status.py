"""Print the status of the Catbus.

This is your first task of the project."""


from .magic import get_destination, get_waiting


def print_status(onboard, location):
    """Print the passengers on the Catbus, where they want to go, the
    stop the Catbus is at, and the passengers waiting at that stop."""
    #<SOLUTION>
    if len(onboard) > 0:
        print(f'The passengers on the Catbus are:')
        for passenger in onboard:
            print(f'\t{passenger} -> {get_destination(passenger)}')

    print(f'The Catbus is at {location}.')

    waiting = get_waiting(location)
    if len(get_waiting(location)) == 1:
        print('There is one person waiting:')
        print(f'\t{waiting[0]} -> {get_destination(waiting[0])}')
    elif len(waiting) > 1:
        print(f'There are {len(waiting)} passengers waiting:')
        for passenger in waiting:
            print(f'\t{passenger} -> {get_destination(passenger)}')
    #</SOLUTION>