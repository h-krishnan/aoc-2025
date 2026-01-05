"""
Advent of Code 2025 - Day 3
Find the largest n-digit number that can be formed from digits in a string.
"""

# Read input from file
inp = open('3.txt').read()

# Toggle for testing with example data
example = 0
if example:
    inp = """
987654321111111
811111111111119
234234234234278
818181911112111
"""

# Parse input into lines
inp = inp.strip().split('\n')

def find_n_digits(string, n):
    """
    Recursively find the largest n-digit number from available digits.
    Strategy: Pick the largest digit first, then recursively solve for remaining digits.
    
    Args:
        string: String of digits to choose from
        n: Number of digits to find
    
    Returns:
        Largest n-digit number that can be formed
    """
    if len(string) == n:
        return int(string)
    
    # Find the largest digit and its position
    mx = 0  # Maximum digit value
    ld = 0  # Position of largest digit
    for c in range(len(string)-n+1):
        if int(string[c]) > mx:
            mx = int(string[c])
            ld = c
    
    if n == 1:
        v = mx
    else:
        # Recursively find remaining digits after the largest one
        v = 10**(n-1)*mx + find_n_digits(string[ld+1:], n-1)
    return v

def part1(inp):
    """
    Find sum of largest 2-digit numbers from each line.
    
    Args:
        inp: List of digit strings
    
    Returns:
        Sum of all 2-digit results
    """
    s = 0
    for l in inp:
        s += find_n_digits(l.strip(), 2)
    return s

def part2(inp):
    """
    Find sum of largest 12-digit numbers from each line.
    
    Args:
        inp: List of digit strings
    
    Returns:
        Sum of all 12-digit results
    """
    s = 0
    for l in inp:
        s += find_n_digits(l.strip(), 12)
    return s

print("Part 1:", part1(inp))
print("Part 2:", part2(inp))
