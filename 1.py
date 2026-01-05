"""
Advent of Code 2025 - Day 1
Circular direction tracking problem with left/right turns.
"""

# Read input from file
inp = open('1.txt').read()

# Toggle for testing with example data
example = 0
if example:
    inp = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

# Parse input into lines
inp = inp.strip()
inp = inp.split('\n')

def part1(inp):
    """
    Count how many times direction returns to starting position (0).
    Direction cycles through 0-99 in a circular manner.
    
    Args:
        inp: List of direction commands (L/R followed by number)
    
    Returns:
        Count of times position returns to 0
    """
    d = 50  # Starting direction
    c = 0   # Count of returns to 0
    for l in inp:
        i = l[0]  # Direction indicator (L or R)
        n = int(l[1:])  # Amount to turn
        if i == 'R':
            d = (d + n) % 100  # Turn right (clockwise)
        else:
            d = (d - n) % 100  # Turn left (counter-clockwise)
        if d == 0:
            c += 1  # Count when we return to starting direction
    return c


def part2(inp):
    """
    Count total number of complete cycles (passing through 0) during movement.
    Tracks when direction value crosses boundaries (0 or 100).
    
    Args:
        inp: List of direction commands (L/R followed by number)
    
    Returns:
        Total number of complete cycles
    """
    d = 50  # Starting direction
    c = 0   # Count of cycles
    for l in inp:
        i = l[0]  # Direction indicator (L or R)
        n = int(l[1:])  # Amount to turn
        if n == 0:
            continue
        if i == 'R':
            d = (d + n)
            if d >= 100:
                c += d // 100  # Count complete cycles going right
                d %= 100
        else:
            d = (d - n)
            if d <= 0:
                c += -d // 100  # Count complete cycles going left
                if d+n != 0:
                    c += 1
            d %= 100
    return c

print (f"Part1: {part1(inp)}")
print (f"Part2: {part2(inp)}")
