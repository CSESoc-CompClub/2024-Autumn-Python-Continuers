"""Pick up and drop off passengers at stops.

This is your third task of the project."""


from .constants import CATPACITY
from .magic import get_waiting


def pick_up(passenger, onboard, stop):
    """Pick up a passenger."""
    #<SOLUTION>
    waiting = get_waiting(stop)
    if passenger in waiting and len(onboard) < CATPACITY:
        waiting.remove(passenger)
        onboard.append(passenger)
    #</SOLUTION>


def drop_off(passenger, onboard, stop):
    """Drop off a passenger."""
    #<SOLUTION>
    waiting = get_waiting(stop)
    if passenger in onboard:
        onboard.remove(passenger)
        waiting.append(passenger)
    #</SOLUTION>