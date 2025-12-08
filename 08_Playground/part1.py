#!/usr/bin/env python3

import math
import sys
from collections import defaultdict

strings = [tuple(map(int, line.split(","))) for line in sys.stdin]
number_of_strings = len(strings)
circuit_id = 0
circuits = {}


def find_all_distances():
    distances = defaultdict(dict)
    for i, j in [
        (i, j)
        for i in range(number_of_strings)
        for j in range(i+1, number_of_strings)
    ]:
        a, b = strings[i], strings[j]
        distance = math.dist(a, b)
        distances[a][b] = distance
    return distances


def create_distance_map(distances):
    distance_map = {}
    for a, other in distances.items():
        for b, distance in other.items():
            # Make an assumption about the puzzle input,
            # that simplifies the data structure here.
            assert distance not in distance_map

            distance_map[distance] = (a,b)
    return distance_map
    

def create_circuit(a, b):
    # Both strings are already connected to a circuit.
    if a in circuits and b in circuits:
        # When they are part of the same circuit, no action is needed.
        if circuits[a] == circuits[b]:
            return

        # Otherwise, put all lights into the same circuit.
        circuit_a = circuits[a]
        circuit_b = circuits[b]
        for n, c in circuits.items():
            if c == circuit_b:
                circuits[n] = circuit_a
    # If A is already in a circuit, then connect B to it too.
    elif a in circuits:
        circuits[b] = circuits[a]
    # If B is already in a circuit, then connect A to it too.
    elif b in circuits:
        circuits[a] = circuits[b]
    # Both A and B are not in a circuit. Put both in a new circuit.
    else:
        global circuit_id
        circuit_id += 1
        circuits[a] = circuit_id
        circuits[b] = circuit_id


distances = find_all_distances()
distance_map = create_distance_map(distances)
sorted_distances = sorted(distance_map.keys())
i = 0
for distance in sorted_distances:
    create_circuit(*distance_map[distance])
    i+=1
    if i == 1000:
        break

circuit_lengths = defaultdict(int)
for circuit_id in circuits.values():
    circuit_lengths[circuit_id] += 1    

sorted = list(reversed(sorted(circuit_lengths.values())))
print(sorted[0] * sorted[1] * sorted[2])

