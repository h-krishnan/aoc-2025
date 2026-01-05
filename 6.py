"""
Advent of Code 2025 - Day 6
Process columnar data with multiplication (*) and addition (+) operations.
"""

# Read input from file
inp = open('6.txt').read()

# Toggle for testing with example data
example = 0
if example:
    inp = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +"""

def compute_value(data, oplist):
    """
    Compute value by applying operations to columns of data.
    
    Args:
        data: List of lists containing numbers for each column
        oplist: List of operations ('*' or '+') to apply
    
    Returns:
        Total computed value
    """
    s = 0
    for d, op in zip(data, oplist):
        if op == '*':
            # Multiply all values in the column
            v = 1
            for x in d:
                v *= x
            s += v
        elif op == '+':
            # Sum all values in the column
            s += sum(d)
        else:
            print("Unvalid op", op)
    return s

def part1(inp):
    """
    Parse data by splitting on spaces (column-aligned).
    
    Args:
        inp: Input string with rows of space-separated numbers and operator row
    
    Returns:
        Computed value based on operations
    """
    inp = inp.strip().split('\n')
    # Create empty lists for each column
    data = list(list() for i in inp[0])
    # Parse all rows except the last (which contains operations)
    for l in inp[:-1]:
        l = [int(x) for x in l.strip().split()]
        for d,i in zip(data, l):
            d.append(i)
    return compute_value(data, inp[-1].strip().split())


def part2(inp):
    """
    Parse data by character position (fixed-width columns).
    Handles variable-width numbers by detecting whitespace boundaries.
    
    Args:
        inp: Input string with rows of numbers and operator row
    
    Returns:
        Computed value based on operations
    """
    inp = inp.strip().split('\n')
    data = list(list() for i in inp[0])
    # Build strings for each character position
    inp1 = ["" for c in inp[0]]
    for l in inp[:-1]:
        for i, c in enumerate(l):
            inp1[i] = inp1[i] + c

    # Split by whitespace to form columns
    data = []
    d = []
    for i in inp1:
        if i.strip() == "":
            data.append(d)
            d = []
        else:
            d.append(int(i))
    data.append(d)

    return compute_value(data, inp[-1].strip().split())

print("Part1:", part1(inp))
print("Part2:", part2(inp))

