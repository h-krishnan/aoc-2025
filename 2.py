"""
Advent of Code 2025 - Day 2
Number pattern matching problem - find numbers with specific properties.
"""

# Read input from file
inp = open('2.txt').read()

# Toggle for testing with example data
example = 0
if example:
    inp = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
"""
# Parse input as comma-separated ranges
inp = inp.strip().split(",")

def solve(inp, part):
    """
    Find numbers in given ranges that match specific patterns.
    
    Part 1: Numbers where first half equals second half (even length only)
    Part 2: Numbers that can be formed by repeating a pattern
    
    Args:
        inp: List of range strings in format "start-end"
        part: Problem part (1 or 2)
    
    Returns:
        Sum of all numbers matching the criteria
    """
    t = 0  # Total sum
    for l in inp:
        i1, i2 = [int(x) for x in l.split("-")]
        # Iterate through range, starting from at least 10
        for x in range(max(i1, 10), i2+1):
            s = str(x)
            if part == 1:
                # Part 1: Check if first half equals second half
                if len(s) % 2 != 0:
                    continue
                if s[:len(s)//2] == s[len(s)//2:]:
                    t += x
            else:
                # Part 2: Check if number can be formed by repeating a substring
                start = 1 if part == 2 else len(s)//2
                for i in range(start, len(s)//2 + 1):
                    s1 = s[:i]*(len(s)//i)  # Repeat pattern
                    if s == s1:
                        t += x
                        break
    return t

print("Part 1:", solve(inp, 1))
print("Part 2:", solve(inp, 2))

