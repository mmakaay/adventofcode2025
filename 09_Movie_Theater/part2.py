#!/usr/bin/env python3

import sys

# Retrieve the set of red tiles.
red_tile_coordinates = [tuple(map(int, line.split(","))) for line in sys.stdin]
red_tiles = set(red_tile_coordinates)
nr_of_red_tiles = len(red_tiles)

# Create the set of green tiles that form connections between the red tiles.
# This should work, looking at the example file that has the connecting red
# tiles in the correct order in its input. Looking at my full input, the same
# tile ordering is used there (seeing matching up x- or y-coordinates between
# follow-up pairs of coordinates.)
green_tiles = set()
for i in range(nr_of_red_tiles):
    from_x, from_y = red_tile_coordinates[i]
    to_x, to_y = red_tile_coordinates[(i + 1) % nr_of_red_tiles]

    # Fill in vertically.
    if from_x == to_x:
        step = 1 if to_y > from_y else -1
        for y in range(from_y, to_y + step, step):
            green_tiles.add((from_x, y))
    # Fill in horizontally.
    else:
        step = 1 if to_x > from_x else -1
        for x in range(from_x, to_x + step, step):
            green_tiles.add((x, from_y))

# Combine these into a set containing all of the edge tiles.
all_edge_tiles = red_tiles | green_tiles

# The grid as a whole is way too big to work with. When trying to process
# the real input, the spacing of the tiles results in an enourmously big grid.
# Here's an idea: we can look at the interesting horizontal and vertical lines,
# to squeeze the grid into a smaller grid. Eh, I described compression :)
#
# Additionally, there is empty space around the outer edges. Looking at the
# real input, it is even more apparent there. We are interested in the maximum
# area possible, not in its exact location. So we can ignore this space.
#
# Given the example grid, these are the interesting lines:
#
#     2    7 9 11
#     v    v v v
#   ..............
# 1>.......#XXX#..
#   .......X...X..
# 3>..#XXXX#...X..
#   ..X........X..
# 5>..#XXXXXX#.X..
#   .........X.X..
# 7>.........#X#..
#   ..............
#
# Compressing would lead to:
#
#  .#X#
#  ##.X
#  #X#X
#  ..##
#
# Decisions on inside-or-outside-the-polygon wouldn't change here.
# They only become less complex, because less of the inside dots
# have to be checked.
#
# Given that after compression, we do see both red (#) and green (@) tiles,
# we will have to investigate the combined red and green edges to decide if
# a position is inside or outside the polygon.
#
# This seems feasible, let's go with this.
#
squeezed_x = sorted(set(x for x, _ in red_tile_coordinates))
squeezed_y = sorted(set(y for _, y in red_tile_coordinates))
squeezed_x_index = {x: i for i, x in enumerate(squeezed_x)}
squeezed_y_index = {y: i for i, y in enumerate(squeezed_y)}
squeezed_width = len(squeezed_x)
squeezed_height = len(squeezed_y)

# Precompute which vertical edges are relevant for each y-coordinate
# in the grid. Using the precomputation, the script finished about
# 5 times faster, so it's a keeper :-)
vertical_edges_by_y = {}
x1, y1 = red_tile_coordinates[-1]
for x2, y2 in red_tile_coordinates:
    # For is_inside_polygon(), we're only interested in the vertical
    # edges. See the documentation for that function to see why.
    if x1 == x2:
        # Add this vertical edge to all y-coordinates it spans
        y_from, y_to = min(y1, y2), max(y1, y2)
        for y in squeezed_y:
            if y_from < y <= y_to:
                vertical_edges_by_y.setdefault(y, []).append(x1)
    x1, y1 = x2, y2


def is_inside_polygon(x: int, y: int) -> bool:
    """
    Decide if a given point is inside the tile edges polygon.

    Method: start at x,y, and trace all the way to the right edge.
    When an odd number of edges has been passed, we must have started
    from inside the polygon.

    For example, in the below diagram, Y is not inside the polygon,
    and it crosses 2 edges. X is inside the polygon, which can be
    determined because it crosses 3 edges (or 1, when going to the
    left, or up or down).

    In this algorithm, horizontal edges can be safely ignored. In the
    example, when tracing Z we end up crossing 1 edge, indicating that
    the point is inside the polygon.

    ........................
    ...#@@@@@#.....#@@@@#...
    ...@.....@.....@....@...
    ...@.....@..Y-(1)--(2)->
    ...@.....@.....@....@...
    ...@..X-(1)---(2)--(3)->
    ...@.....@.....@....@...
    ...@..Z--#@@@@@#---(1)->
    ...@................@...
    ...#@@@@@@@@@@@@@@@@#...
    ........................

    Update: looks I invented a simplified form of the "Ray casting
    algorithm". See: https://en.wikipedia.org/wiki/Point_in_polygon
    Simplified, because ray casting also works for angled lines.
    """
    # Look up the vertical edges that span the y-coordinate.
    relevant_edges = vertical_edges_by_y.get(y, [])

    # Count how many of these edges are at or to the right of x.
    crossings = sum(x <= edge_x for edge_x in relevant_edges)

    # Odd crossings => inside, even => outside.
    return crossings & 1


# Now we have the compressed data, create a grid in which we can write
# the compressed decisions on inside or outside the polygon. Not sure if
# this is the optimal way for it, but time will tell (quite literally).
# For my puzzle input, the final decision grid has 61504 positions.
# Quite a few, but not extremely bad either.
insides = [[False] * squeezed_width for _ in range(squeezed_height)]
for i, y in enumerate(squeezed_y):
    for j, x in enumerate(squeezed_x):
        # If we're on an edge tile, we're inside the polygon by definition.
        if (x, y) in all_edge_tiles:
            insides[i][j] = True
        # Otherwise, we have to actively trace the position to decide on it.
        elif is_inside_polygon(x, y):
            insides[i][j] = True


def is_rectangle_valid(x1, y1, x2, y2):
    """
    Check if all cells in the compressed rectangle are valid.

    Loop through each cell in the rectangle to check validity.
    This does not feel extremely optimal, but with only a few seconds
    run time for this script when using the full input, I am happy with it.
    """
    return all(
        insides[y][x]
        for y in range(y1, y2 + 1)
        for x in range(x1, x2 + 1)
    )


# Getting there! We now have enough building blocks to start our
# search for the largest possible rectangle.
best_area = 0
for i, j in [
    (i, j)
    for i in range(nr_of_red_tiles)
    for j in range(i+1, nr_of_red_tiles)
]:
    x1, y1 = red_tile_coordinates[i]
    x2, y2 = red_tile_coordinates[j]

    # Skip if smaller than the currently best area.
    area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
    if area <= best_area:
        continue

    # Transpose to the compressed grid coordinates.
    x1, y1 = squeezed_x_index[x1], squeezed_y_index[y1]
    x2, y2 = squeezed_x_index[x2], squeezed_y_index[y2]

    # Normalize the coordinates to be from top left to bottom right.
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    # Check if rectangle contains only valid tiles.
    if is_rectangle_valid(x1, y1, x2, y2):
        best_area = area

print(best_area)
