#!/usr/bin/env python3

import re
import sys
from typing import Generator


# Read input.
ranges = [
    tuple(map(int, r.split("-")))
    for r
    in next(sys.stdin).split(",")
]

# Find invalid numbers.
HAS_REPEATED_DOUBLES = re.compile(r"^(\d+)\1+$")
total = 0
for a, b in ranges:
    while a <= b:
        if HAS_REPEATED_DOUBLES.match(str(a)):
            total += a
        a += 1

print(total)

