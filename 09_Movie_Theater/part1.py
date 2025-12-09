#!/usr/bin/env python3

import sys
import math

red_tiles = [tuple(map(int, line.split(","))) for line in sys.stdin]
nr_of_red_tiles = len(red_tiles)

max_area = 0

for i, j in [
    (i, j)
    for i in range(nr_of_red_tiles)
    for j in range(i+1, nr_of_red_tiles)
]:
    xa, ya = red_tiles[i]
    xb, yb = red_tiles[j]
    area = (1 + abs(xb - xa)) * (1 + abs(yb - ya))
    if area > max_area:
        max_area = area

print(max_area)


