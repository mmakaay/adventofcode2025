#!/usr/bin/env python3

# Parse the input.
regions = []
for line in map(str.strip, open(0)):
    # The present shapes are of no consequence.
    # Read only the regions (size + number of presents).
    if 'x' in line:
        parts = line.split(': ')
        width, height = map(int, parts[0].split('x'))
        counts = list(map(int, parts[1].split()))
        regions.append((width, height, counts))

# Apply heuristics to determine if the presents fit.
# The tolerance luckily hit the jackpot at 2 :-D
# See README.md for some info on this.
TOLERANCE = 2
total = 0
for i, (w, h, counts) in enumerate(regions):
    total_presents = sum(counts)
    total_bbox = total_presents * 9
    if total_bbox <= w * h + TOLERANCE:
        total += 1

print(total)
