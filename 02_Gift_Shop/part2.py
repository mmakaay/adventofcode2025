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
total = 0
for a, b in ranges:
    while a <= b:
        if re.match(r"^(\d+)\1+$", str(a)):
            total += a
        a += 1

print(total)

