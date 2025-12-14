This is a knapsack problem, and given the sheer number of 
presents to fit in the areas, we won't be able to solve
this by actually rotating and fitting presents in the areas.

Interesting observation: In the input, all present bounding
boxes are 3x3, both in the example and my personal puzzle.

The example explains:

a) 4x4: 0 0 0 0 2 0   -> fits
b) 12x5: 1 0 1 0 2 2  -> fits
c) 12x5: 1 0 1 0 3 2  -> no fit

Some stats:

a) 4x4 = 16, presents size 14, block size 18
b) 12x5 = 60, presents size 35, block size 54
c) 12x5 = 60, presents size 49, block size 63

The presents size doesn't look very feasible for a heuristic
approach. All sizes fall below the available space. For a),
we can only add 2, before reaching the available space. Using
this number brings b) to 37 and c) to 51. All still under the
available space.

Total block size seems to be close though...

When subtracting 1:

a) 18-1=17  -> above area 16 -> fail
b) 54-1=53  -> below area 60 -> success
c) 63-1=62  -> above area 60 -> success

When subtracting 2:

a) 18-2=16  -> equal to area 16 -> success
b) 54-2=52  -> below area 60 -> success
c) 63-2=61  -> above area 60 -> success

When subtracting 3:

a) 18-3=15  -> below area 16 -> success
b) 54-3=51  -> below area 60 -> success
c) 63-3=60  -> equal to area 60 -> fail

When subtracting 4:

a) 18-4=14  -> below area 16 -> success
b) 54-4=50  -> below area 60 -> success
c) 63-4=59  -> below area 60 -> fail

**Conclusion:** A tolerance of 2 seems feasible.

**Spoiler:** I coded the solution, and 2 worked
like a charm for my personal puzzle input.

**Update:** I found that the example requires tolerance 2,
but that the real puzzle input works with 0 - 458!

