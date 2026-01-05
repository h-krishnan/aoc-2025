"""
Advent of Code 2025 - Day 11
Device connection graph problem - count paths through network.
Part 1: Count paths from 'you' to 'out'.
Part 2: Count product of paths through specific intermediate nodes.
"""

import functools
import time

# Read input from file
inp = open('11.txt').read().strip()

inp = inp.strip().split('\n')

# Parse device connection graph
# Format: "device: connection1 connection2 ..."
devices = {}
for l in inp:
    l = l.strip().split()
    s = l[0][:-1]  # Remove trailing colon
    devices[s] = l[1:]  # List of connections

@functools.cache
def connection_count(source, target):
    """
    Recursively count number of paths from source to target device.
    Uses memoization to avoid recalculating same paths.
    
    Args:
        source: Starting device name
        target: Target device name
    
    Returns:
        Number of distinct paths from source to target
    """
    return 1 if source == target else \
            sum(connection_count(v, target)
                for v in devices.get(source, []))

def part1():
    """
    Count paths from 'you' to 'out'.
    
    Returns:
        Number of paths
    """
    return connection_count('you', 'out')

def part2():
    """
    Calculate product of path counts through specific checkpoints.
    Tries two different path sequences: svr->dac->fft->out or svr->fft->dac->out.
    
    Returns:
        Product of path counts through checkpoints
    """
    # Try first path sequence
    a = connection_count('svr', 'dac')
    if a:
        b = connection_count('dac', 'fft')
        if b:
            c = connection_count('fft', 'out')
            if c:
                 return a*b*c
    # Try alternative path sequence
    d = connection_count('svr', 'fft')
    e = connection_count('fft', 'dac')
    f = connection_count('dac', 'out')

    return d*e*f

print("Part1:", part1())
print("Part2:", part2())





