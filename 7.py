"""
Advent of Code 2025 - Day 7
Beam propagation simulation with splitters in a grid.
Part 1: Count beam splits; Part 2: Count ways beams reach final positions.
"""

# Read input from file
inp = open('7.txt').read()

# Toggle for testing with example data
example = 0
if example:
    inp = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

inp = inp.strip()
inp = inp.split('\n')

# Parse grid to find beams (S) and splitters (^)
beams = set()
splitters = set()

for i,l in enumerate(inp):
    for j, c in enumerate(l.strip()):
        if c == 'S':
            beams.add((i,j))
        elif c == '^':
            splitters.add((i,j))

# Grid dimensions
imax = i
jmax = j

def print_beams():
    """Helper function to visualize beam positions (for debugging)."""
    for i in range(imax):
      for j in range(jmax):
        if (i,j) in beams:
            print("|", end="")
        elif (i,j) in splitters:
            print("^", end="")
        else:
            print(".", end="")
      print()
    print()

# Track all beam positions throughout simulation
all_beams = set()
all_beams |= beams
splits = 0  # Count of beam splits
p = 1  # Current row/iteration

# Simulate beam propagation downward
while True:
    if p > imax:
        break
    p += 1
    beams = set((i,j) for i,j in beams)
    new_beams = set()
    for i,j in beams:
        # Check if next position has a splitter
        if (i+1,j) in splitters:
            splits += 1
            # Beam splits to left and right
            if j > 0:
                new_beams.add((i+1,j-1))
            if j < jmax:
                new_beams.add((i+1,j+1))
        else:
            # Beam continues straight down
            new_beams.add((i+1,j))
    beams = new_beams
    all_beams |= beams

print("Part1:", splits)


# Part 2: Count number of ways to reach each final beam position
import functools
@functools.cache
def n_ways(beam):
    """
    Recursively count paths to reach a beam position.
    
    Args:
        beam: (row, col) position of beam
    
    Returns:
        Number of distinct paths to reach this position
    """
    i, j = beam
    if i == 0:
        return 1  # Starting position has one way to reach it
    s = 0
    # Can come from directly above
    if (i-1, j) in all_beams:
        s += n_ways((i-1,j))

    # Can come from splitter on left
    if (i,j-1) in splitters and (i-1,j-1) in all_beams:
        s += n_ways((i-1,j-1))
    # Can come from splitter on right
    if (i,j+1) in splitters and (i-1,j+1) in all_beams:
        s += n_ways((i-1,j+1))
    return s

# Calculate total ways for all final beams
beams = sorted(beams, key=lambda x:x[1])
s= 0
for b in beams:
    n = n_ways(b)
    s += n

print("Part2:", s)
