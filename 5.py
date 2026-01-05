"""
Advent of Code 2025 - Day 5
Range intersection problem - count IDs in ranges and calculate total range coverage.
"""

# Read input from file
inp = open('5.txt').read()

# Toggle for testing with example data
example = 0
if example:
    inp = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

# Parse input into ranges and IDs
ranges = []
ids = []
for l in inp.split():
    if not l:
        continue
    if '-' in l:
        ranges.append(tuple(int(x) for x in l.strip().split('-')))
    else:
        ids.append(int(l.strip()))


def part1():
    """
    Count how many IDs fall within at least one range.
    
    Returns:
        Count of IDs that are within any range
    """
    count = 0
    for i in ids:
        for r in ranges:
            # Check if ID falls within range (inclusive)
            if i >= r[0] and i <= r[1]:
                count += 1
                break
    return count


def part2():
    """
    Calculate total coverage of all ranges (handling overlaps).
    Uses a sweep line algorithm with depth tracking.
    
    Returns:
        Total number of integers covered by all ranges
    """
    # Create events: +1 at range start, -1 at range end
    lst = [(r[0],1) for r in ranges] + [(r[1],-1) for r in ranges]
    lst.sort(key = lambda x: x[0])

    count = 0
    depth = 0  # How many overlapping ranges
    curr = 0   # Current range start position
    for l,s in lst:
        if s == -1:
            depth -= 1
            # When depth reaches 0, we're exiting all ranges
            if depth == 0:
                count += l - curr + 1
        elif s == 1:
            depth += 1
            # When depth becomes 1, we're entering a new coverage area
            if depth == 1:
                curr = l
    return count

print("Part1:", part1())
print("Part2:", part2())

        


