#!/usr/bin/env python3

from collections.abc import Generator

import sys

grid = [list(line.strip()) for line in sys.stdin]
size_x = len(grid[0])
size_y = len(grid)


def count_surrounding_rolls(at_x: int, at_y: int) -> int:
    return sum(has_roll(x, y) for x, y in surroundings(at_x, at_y))
         

def has_roll(at_x: int, at_y: int) -> bool:
    return grid[at_y][at_x] == "@"


def surroundings(at_x: int, at_y: int) -> Generator[tuple[int, int]]:
    directions = [
        (0, -1), (1, -1), (1, 0), (1, 1),
        (0, 1), (-1, 1), (-1, 0), (-1, -1),
    ]
    for dx, dy in directions:
        x, y = at_x + dx, at_y + dy
        if 0 <= x < size_x and 0 <= y < size_y:
            yield x, y


def can_move(at_x: int, at_y: int) -> bool:
    return count_surrounding_rolls(at_x, at_y) < 4


def remove_roll(at_x: int, at_y: int) -> None:
    grid[at_y][at_x] = "."


removed_rolls = 0

while True:
    removable_rolls = [
        (x, y)
        for y in range(size_y)
        for x in range(size_x)
        if has_roll(x, y) and can_move(x, y)
    ]

    if not removable_rolls:
        break

    for x, y in removable_rolls:
        remove_roll(x, y)
        removed_rolls += 1

print(removed_rolls)
