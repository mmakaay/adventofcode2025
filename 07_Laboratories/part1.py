#!/usr/bin/env python3

import sys

first_line = next(sys.stdin).strip()
starting_beam = first_line.index("S")
width = len(first_line)

beams = [0]*width
beams[starting_beam] = 1

splits = 0

for line in map(str.strip, sys.stdin):
    for i in range(width):
        if line[i] == "^" and beams[i]:
            beams[i] = 0
            beams[i-1] = 1
            beams[i+1] = 1
            splits += 1

print(splits)



