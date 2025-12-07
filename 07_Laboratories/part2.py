#!/usr/bin/env python3

import sys
from functools import cache

lines = tuple(map(str.strip, sys.stdin))
width = len(lines[0])
height = len(lines)


# This method uses memoization to reuse partial results.
@cache
def backtrace_from(x: int, y: int) -> int:
    """
    From a grid position, backtrace and count the number of
    possible routes to starting point "S".
    """
    # We've reached the first line without finding the "S".
    # This was not a valid route. Report zero routes.
    if y == 0:
        return 0

    # The "S" is right above the current grid position X.
    # We found a valid route! Report one route, since there is
    # always only one "S" on the first line.
    #
    # ..S..
    # ..X..
    if lines[y-1][x] == "S":
        return 1

    # Check how many valid routes we can find from the current
    # grid position.
    possible_routes = 0

    # Is there a splitter diagonally to the left of the current
    # grid position X, then we can continue the route from its
    # input position Y.
    #
    # .Y..
    # .^..
    # ..X.
    if x > 0 and lines[y-1][x-1] == "^":
        possible_routes += backtrace_from(x-1, y-2)

    # If there is an empty spot above the current grid position X,
    # then we can continue to route from that empty spot Y.
    #
    # .Y..
    # .X..
    # ....
    if lines[y-1][x] == ".":
        possible_routes += backtrace_from(x, y-1)

    # Is there a splitter diagonally to the right of the current
    # grid position X, then we can continue the route from its
    # input position Y.
    #
    # ..Y.
    # ..^.
    # .X..
    if x < width-1 and lines[y-1][x+1] == "^":
        possible_routes += backtrace_from(x+1, y-2)

    return possible_routes


# Trace back the number of universes from each endpoint.
universes = sum(backtrace_from(i, height-1) for i in range(width))

print(universes)
