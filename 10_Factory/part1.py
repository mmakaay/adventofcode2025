#!/usr/bin/env python3

import sys
import re
from itertools import combinations

def start_machine(required_lights, buttons) -> int:
    # Since XOR is commutative and idempotent (A^A=0), pressing buttons in
    # different orders gives the same result, and pressing twice cancels out.
    # Therefore, we can try out the combinations for these buttons.
    # Since we're looking for the minimnum number of button presses, we start
    # out with the smallest subsets and work our way up.
    for num_buttons in range(len(buttons) + 1):
        for pressed_buttons in combinations(buttons, num_buttons):
            active_lights = 0
            for button in pressed_buttons:
                active_lights ^= button
            if active_lights == required_lights:
                return num_buttons

    raise RuntimError("No solution found! This should never happen.")


def lights_to_int(lights) -> int:
    i = 0
    for bit, state in enumerate(lights):
        if state == "#":
            i += 2 ** bit
    return i


def buttons_to_int(buttons) -> int:
    i = 0
    for bit in buttons:
        i += 2 ** bit
    return i


# Parse input.
# We have at max 10 lights. Toggling these is a perfect job for XOR.
# Therefore, I translate the lights and buttons into integer values.
machines = []
for line in sys.stdin:
    parts = line.split()
    lights = lights_to_int(parts.pop(0)[1:-1])
    buttons = [buttons_to_int(map(int, p[1:-1].split(","))) for p in parts]
    machines.append((lights, buttons))


# Start machines.
total_button_presses = sum(
    start_machine(lights, buttons)
    for lights, buttons
    in machines
)

print(total_button_presses)
