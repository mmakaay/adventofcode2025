#!/usr/bin/env python3

import re
import sys
from functools import cache


graph = dict()

for line in sys.stdin:
    source, *destinations = re.split(r"\W+", line.strip())
    graph[source] = destinations


@cache
def find_routes(source, destination) -> int:
    if source == destination:
        return 1
    if source not in graph:
        return 0

    routes = 0
    for next_node in graph[source]:
        routes += find_routes(next_node, destination)
    return routes


# Compute: svr -> dac -> fft -> out
via_dac_fft = (
    find_routes("svr", "dac") *
    find_routes("dac", "fft") *
    find_routes("fft", "out")
)

# Compute: svr -> fft -> dac -> out
via_fft_dac = (
    find_routes("svr", "fft") *
    find_routes("fft", "dac") *
    find_routes("dac", "out")
)

print(via_dac_fft + via_fft_dac)

