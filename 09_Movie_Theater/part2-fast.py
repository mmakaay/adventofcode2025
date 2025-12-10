#!/usr/bin/env python3

import sys

# Retrieve the set of red tiles (polygon vertices).
red_tile_coordinates = [tuple(map(int, line.split(","))) for line in sys.stdin]
nr_of_red_tiles = len(red_tile_coordinates)

# Rather than computing inside/outside for all grid points (which would
# require a huge grid due to sparse coordinates), we can use a faster
# approach: build a list of polygon edges, and check if any edges cross
# through a rectangle's interior. If no edges cross, the rectangle is valid!
# This works directly with the original coordinates without compression.
#
# Build the polygon edges from consecutive red tiles. Since the red tiles
# are already in order, we just connect each tile to the next one.
polygon_edges = list(sorted(
    zip(
        red_tile_coordinates,
        red_tile_coordinates[1:] + red_tile_coordinates[:1]
    ),
    # This sorting gives me the best results. This might be related
    # to my specific data set.
    key=lambda a: a[1][0]-a[0][0],
))


def edge_crosses_rectangle(edge, min_x, max_x, min_y, max_y):
    (x1, y1), (x2, y2) = edge

    # Vertical edge.
    if x1 == x2:
        x = x1
        y_from, y_to = min(y1, y2), max(y1, y2)
        return min_x < x < max_x and y_to > min_y and y_from < max_y

    # Horizontal edge.
    else:
        y = y1
        x_from, x_to = min(x1, x2), max(x1, x2)
        return y > min_y and y < max_y and x_to > min_x and x_from < max_x


def is_rectangle_valid(p1, p2):
    min_x = min(p1[0], p2[0])
    max_x = max(p1[0], p2[0])
    min_y = min(p1[1], p2[1])
    max_y = max(p1[1], p2[1])

    for edge in polygon_edges:
        if edge_crosses_rectangle(edge, min_x, max_x, min_y, max_y):
            return False

    return True


# Search for the largest possible rectangle.
best_area = 0
for i, j in [
    (i, j)
    for i in range(nr_of_red_tiles)
    for j in range(i+1, nr_of_red_tiles)
]:
    p1 = red_tile_coordinates[i]
    p2 = red_tile_coordinates[j]

    # Skip if smaller than the currently best area.
    area = (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)
    if area <= best_area:
        continue

    # Check if rectangle is valid (no edges cross through it).
    if is_rectangle_valid(p1, p2):
        best_area = area

print(best_area)
