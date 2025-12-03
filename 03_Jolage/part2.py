#!/usr/bin/env python3

import sys

total = 0

INCLUDE_BATTERIES = 12

for batteries in map(str.strip, sys.stdin):
    best_batteries = []

    for preserve in range(INCLUDE_BATTERIES, 0, -1):
        # When we have exactly as many batteries left to inspect,
        # as the number of batteries that are required, then no
        # further inspection is required.
        if preserve == len(batteries):
            best_batteries.extend(batteries)
            break

        # Look at the remaining available batteries in the bank,
        # disregarding the number of batteries at the end that we
        # still require to build the full battery pack.
        applicable_batteries = batteries[:len(batteries)-preserve+1]
        best_battery = max(applicable_batteries)
        best_batteries.append(best_battery)
        earliest_position_for_best_battery = applicable_batteries.index(best_battery)

        # Narrow our view to the batteries that come after the battery that we found.
        batteries = batteries[earliest_position_for_best_battery + 1:]

    joltage = int("".join(best_batteries))
    total += joltage

print(total)

