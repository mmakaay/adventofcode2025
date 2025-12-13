#!/usr/bin/env python3

import re
import sys

graph = dict()
for line in sys.stdin:
    source, *destinations = re.split(r"\W+", line.strip())
    graph[source] = destinations


def find_routes(node) -> int:
    if node == "out":
        return 1
    routes = 0
    for next_node in graph[node]:
        routes += find_routes(next_node)
    return routes

print(find_routes("you"))
