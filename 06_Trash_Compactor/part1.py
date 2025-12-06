#!/usr/bin/env python3

import sys
from operator import mul, add
from functools import reduce

total = 0

lines = [line.split() for line in sys.stdin]
for *numbers, operator in zip(*lines):
    operation = mul if operator == '*' else add
    numbers_as_int = map(int, numbers)
    result = reduce(operation, numbers_as_int)
    total += result

print(total)

