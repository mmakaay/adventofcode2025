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
    if a in circuits and b in circuits:
        # Already in same circuit.
        if circuits[a] == circuits[b]:
            return

        # Connect partial circuits.
        circuit_a = circuits[a]
        circuit_b = circuits[b]
        for n, c in circuits.items():
            if c == circuit_b:
                circuits[n] = circuit_a
    elif a in circuits:
        circuits[b] = circuits[a]
    elif b in circuits:
        circuits[a] = circuits[b]
    else:
        global circuit_id
        circuit_id += 1
        circuits[a] = circuit_id
        circuits[b] = circuit_id


distances = find_all_distances()
distance_map = create_distance_map(distances)
sorted_distances = sorted(distance_map.keys())
for distance in sorted_distances:
    # Add new connection to the circuit.
    a, b = distance_map[distance]
    create_circuit(a, b)

    # Full circuit accomplished?
    if len(circuits) == len(strings): 
        if len(set(circuits.values())) == 1:
            # Yes! Report the requested distance.
            result = a[0] * b[0]
            print(result)
            break

