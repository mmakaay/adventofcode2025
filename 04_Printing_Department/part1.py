#!/usr/bin/env python3

from collections.abc import Generator

import sys

grid = list(map(str.strip, sys.stdin.readlines()))
width = len(grid[0])
height = len(grid)


def surroundings(at_x: int, at_y: int) -> Generator[tuple[int, int]]:
    directions = [
        (0, -1), (1, -1), (1, 0), (1, 1),
        (0, 1), (-1, 1), (-1, 0), (-1, -1),
    ]
    for dx, dy in directions:
        x, y = at_x + dx, at_y + dy
        if 0 <= x < width and 0 <= y < height:
            yield x, y


def has_roll(at_x: int, at_y: int) -> bool:
    return grid[at_y][at_x] == "@"


def count_surrounding_rolls(at_x: int, at_y: int) -> int:
    return sum(has_roll(x, y) for x, y in surroundings(at_x, at_y))
         

def can_move(at_x: int, at_y: int) -> bool:
    return count_surrounding_rolls(at_x, at_y) < 4


accessible_rolls = sum(
    has_roll(x, y) and can_move(x, y)
    for y in range(height)
    for x in range(width)
)

print(accessible_rolls)
