#!/usr/bin/env python3

import sys
import pulp

def start_machine(joltages, buttons):
    # Initialize a minimization problem.
    problem = pulp.LpProblem("power_up_machine", pulp.LpMinimize)

    # The variables to resolve represent the number of button presses.
    # Create a variable for each of the buttons.
    presses_per_button = [
        pulp.LpVariable(
            f"presses_on_{button_idx}",
            lowBound=0, # No negative button presses
            cat='Integer',
        )
        for button_idx in range(len(buttons))
    ]

    # Add these variables as the objective for the problem.
    # This states that the sum of button presses must be minimized.
    problem += pulp.lpSum(presses_per_button)

    # Create a constraoint for each of the requested joltages.
    for pos, joltage in enumerate(joltages):

        # Look up which of the variables are related to the buttons that
        # increment the current joltage.
        buttons_that_increment_joltage = [
            presses_per_button[button_idx]
            for button_idx, button in enumerate(buttons)
            if pos in button
        ]

        # Since a button press increments a joltage with one, we can state
        # that the sum of the variables must be equal to the required joltage.
        problem += pulp.lpSum(buttons_that_increment_joltage) == joltage

    # Okay, go fetch!!
    problem.solve(pulp.PULP_CBC_CMD(msg=0))

    # This is AoC, this will not fail.
    assert pulp.LpStatus[problem.status] == 'Optimal'

    # Optimal solution found, return the sum of button presses.
    return int(sum(x.varValue for x in presses_per_button))


# Parse input
machines = []
for line in sys.stdin:
    parts = line.split()[1:]
    joltages = [int(j) for j in parts.pop()[1:-1].split(",")]
    buttons = [tuple(map(int, p[1:-1].split(","))) for p in parts]
    machines.append((joltages, buttons))

# Start machines.
total_button_presses = sum(
    start_machine(joltages, buttons)
    for joltages, buttons
    in machines
)

print(total_button_presses)
