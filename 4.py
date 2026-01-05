"""
Advent of Code 2025 - Day 4
Grid simulation where rolls (@) are removed based on neighbor count.
"""

# Read input from file
inp = open('4.txt').read()

# Toggle for testing with example data
example = 0
if example:
    inp = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

# Parse grid into list of lines
inp = inp.strip().split()

# Store positions of rolls (@) as a set of coordinates
rolls = set()
for i, l in enumerate(inp):
    for j, c in enumerate(l.strip()):
        if c == '@':
            rolls.add((i, j))
        elif c == '.':
            pass
        else:
            print (f"Wrong {c} at {i},{j}")

# Grid dimensions
maxx = len(inp[0])
maxy = len(inp)

def solve(rolls, part):
    """
    Simulate removal of rolls with fewer than 4 neighbors.
    
    Part 1: Remove rolls once (one iteration)
    Part 2: Remove rolls repeatedly until no more can be removed
    
    Args:
        rolls: Set of (row, col) coordinates containing rolls
        part: Problem part (1 or 2)
    
    Returns:
        Count of rolls removed
    """
    count = 0
    while True:
        movable = set()
        # Check each position in the grid
        for i in range(maxy):
            for j in range(maxx):
                if (i,j) in rolls:
                    # Count neighbors in all 8 directions
                    c1 = 0
                    for (ii, jj) in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                        if (i+ii, j+jj) in rolls:
                            c1 += 1
                    # Remove rolls with less than 4 neighbors
                    if c1 < 4:
                        count += 1
                        movable.add((i,j))
        if not movable:
            break
        # Remove the marked rolls
        rolls -= movable
        movable.clear()
        if part == 1:
            break  # Part 1: only one iteration
    return count

def print_rolls():
    """Helper function to visualize the grid (for debugging)."""
    for i in range(maxy):
        for j in range(maxx):
            if (i,j) in movable:
                print('x', end="")
            elif (i,j) in rolls:
                print('@', end="")
            else:
                print('.', end="")
        print()
    print()

print("Part1:", solve(rolls.copy(), 1))
print("Part2:", solve(rolls.copy(), 2))
    
