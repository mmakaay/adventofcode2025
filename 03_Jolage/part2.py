#!/usr/bin/env python3

import sys

total = 0

NUMBER_OF_CELLS = 12

for cells in map(str.strip, sys.stdin):
    best_cells = []

    for todo in range(NUMBER_OF_CELLS, 0, -1):
        # When we have exactly as many cells left as the number
        # of cells that are required, then we are done.
        if todo == len(cells):
            best_cells.extend(cells)
            break

        # Look at the remaining available cells in the bank,
        # disregarding the minimal number of cells at the end
        # that we still require to build the full battery pack.
        available_cells = cells[:len(cells)-todo+1]
        best_cell = max(available_cells)
        best_cells.append(best_cell)

        # Narrow our view to only the cells that follow the cell that we found.
        position_of_best_cell = available_cells.index(best_cell)
        cells = cells[position_of_best_cell + 1:]

    joltage = int("".join(best_cells))
    total += joltage

print(total)

