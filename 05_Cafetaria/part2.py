#!/usr/bin/env python3

import sys

data = sys.stdin.read()
fresh, _ = data.split("\n\n") 
fresh = sorted(tuple(map(int, x.split("-"))) for x in fresh.split())

def scan() -> int:
    count = 0
    while fresh:
        # Take the next range.
        start, end = fresh.pop(0)

        # Extend the range with overlapping ranges.
        start, end = scan_overlap(start, end)

        count += end - start + 1
    return count

def scan_overlap(start, end) -> tuple[int, int]:
    # No more ranges available? Then we're done!
    if not fresh:
        return start, end

    # Peek at the next range, to see if its start is inside the current range.
    next_start, next_end = fresh[0]
    if start <= next_start <= end:
        # It is, we have overlap! Move the end of the range if the end of
        # the next range lies beyond the current range.
        fresh.pop(0)
        if next_end > end:
            end = next_end

        # Recurse, to see if there are any more overlaps.
        return scan_overlap(start, end)
   
    # The next range does not overlap. Report the range that was found.
    return start, end
        
print(scan())
