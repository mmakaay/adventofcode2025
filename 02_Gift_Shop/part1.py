#!/usr/bin/env python3

import sys
from typing import Generator


def main() -> None:
    ranges = get_input()
    sum = 0
    for invalid in find_invalid_in_ranges(ranges):
        sum += int(invalid)
    print(sum)


def get_input() -> list[tuple[str, str]]:
    return [
        tuple(r.split("-"))
        for r
        in next(sys.stdin).split(",")
    ]


def find_invalid_in_ranges(range: list[tuple[int, int]]) -> Generator[int]:
    for a, b in range:
        for invalid in find_invalid_in_range(a, b):
            yield invalid


def find_invalid_in_range(a: str, b: str) -> Generator[int]:
    int_b = int(b)

    if is_invalid(a):
        yield a

    while True:
        a = find_next_invalid(a)
        if int(a) > int_b:
            return
        yield a


def is_invalid(a: str) -> bool:
    half = len(a) // 2
    return a[:half] == a[half:]


def find_next_invalid(a: str) -> str:
    if is_odd(len(a)):
        return find_next_invalid("1" + "0" * len(a))

    l = len(a) // 2
    start_half = a[:l]
    end_half = a[l:]

    if not is_invalid(a) and start_half > end_half:
        return start_half + start_half

    next_half = str(int(start_half) + 1) 
    if len(next_half) == len(start_half):
        return next_half + next_half
     
    return find_next_invalid(a + "00")


def is_odd(n) -> bool:
    return n % 2 == 1


if __name__ == "__main__":
    main()

