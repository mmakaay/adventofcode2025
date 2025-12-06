#!/usr/bin/env python3

import sys
from operator import mul, add


def process_worksheet(worksheet):
    rotated_worksheet = zip(*worksheet)

    for *digits, operator in rotated_worksheet:
        operation = mul if operator == '*' else add
        result = join_to_int(digits)
    
        for *digits, _ in rotated_worksheet:
            if at_end_of_problem(digits):
                yield result
                break
            result = operation(result, join_to_int(digits))


def join_to_int(digits):
    return int("".join(digits))


def at_end_of_problem(digits):
    return ''.join(digits).strip() == ""


worksheet = sys.stdin.readlines()
total = sum(process_worksheet(worksheet))
print(total)
