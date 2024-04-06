"""Some magic functions for convenience."""


from collections import defaultdict


# We haven't introduced many data structures to students prior to this
# project. The global variables are unfortunate, but it makes the
# experience smoother for the students. Prefix with an underscore to
# dissuade students from importing this directly, either by a typo, or
# from curiosity.
_destinations = {}
_waiting = defaultdict(list)


def get_destination(passenger):
    """Return the destination of a passenger."""
    return _destinations[passenger]


def get_waiting(stop):
    """Return the passengers waiting at a stop."""
    return _waiting[stop]
