"""Detect if the game has finished.

This is your fifth and final task of the project."""


from .constants import STOPS
from .magic import get_destination, get_waiting


def game_is_finished(onboard):
    """Return whether the game has finished."""
    #<SOLUTION>
    for stop in STOPS:
        for passenger in get_waiting(stop):
            if get_destination(passenger) != stop:
                return False
    return len(onboard) == 0
    #</SOLUTION>