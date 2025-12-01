#!/usr/bin/env python3

import sys

zeroes = 0
position = 50

for line in sys.stdin:
    direction = line[0]
    amount = int(line[1:])
    if direction == 'L':
        amount = -1 * amount
    position = (position + amount) % 100
    if position == 0:
        zeroes += 1

print(f"Result: {zeroes}")


