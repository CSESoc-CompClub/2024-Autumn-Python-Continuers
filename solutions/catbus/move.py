"""Move the Catbus from stop to stop.

This is your fourth task of the project."""


from .constants import STOPS


def find_left_stop(location):
    """Find the stop to the left of the Catbus."""
    #<SOLUTION>
    for i in range(1, len(STOPS)):
        if STOPS[i] == location:
            return STOPS[i - 1]
    #</SOLUTION>


def find_right_stop(location):
    """Find the stop to the right of the Catbus."""
    #<SOLUTION>
    for i in range(0, len(STOPS) - 1):
        if STOPS[i] == location:
            return STOPS[i + 1]
    #</SOLUTION>