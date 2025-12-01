#!/usr/bin/env python3

import sys

zeroes = 0
position = 50

for line in sys.stdin:
    # Parse the instruction.
    direction = line[0]
    amount = int(line[1:])
    sign = -1 if direction == 'L' else +1

    # Carefully rotate the dial, to count the number of zeroes that we see.
    while amount:
        # How far are we away from the next zero in the turning direction?
        distance_to_zero = 100 - position if direction == 'R' else position
        if distance_to_zero == 0:
            distance_to_zero = 100

        # Turn at most to the next zero, given the remaining amount for
        # the current instruction.
        turn = min(distance_to_zero, amount)
        position = (position + sign * turn) % 100
        amount = amount - turn

        # Count the zeroes that we see.
        if position == 0:
            zeroes += 1

print(f"Result: {zeroes}")

