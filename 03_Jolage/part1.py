#!/usr/bin/env python3

import sys

total = 0

for bank in map(str.strip, sys.stdin):
    b1 = max(b for b in bank)
    pos1 = bank.index(b1)
    if pos1 < len(bank) - 1:
        bank_right = bank[pos1+1:]
        b2 = max(b for b in bank_right)
    else:
        b1 = max(b for b in bank[:-1])
        b2 = bank[-1] 
    joltage = int(b1 + b2)
    total += joltage

print(total)

