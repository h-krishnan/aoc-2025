"""
Advent of Code 2025 - Day 12
Box packing problem - determine if boxes can fit in grids.
Part 1: Quick feasibility check based on area and box patterns.
"""

import math
import itertools
import functools
import time

# Read input from file
inp = open('12.txt').read().strip()

inp = inp.split('\n')

# Parse box patterns and grid configurations
boxes = {}  # Box patterns (3x3 grids)
grids = []  # Grid dimensions and required boxes

for i in range(len(inp)):
    l = inp[i].strip()
    if ':' in l:
        if 'x' not in l:
            # Parse box pattern (3x3 grid with # for filled cells)
            bn = int(l[:-1])
            p = [0]*9
            for k in range(3):
                i = i+1
                for j,c in enumerate(inp[i].strip()):
                    if c == '#':
                        p[k*3 + j] = 1
            boxes[bn] = p
        else:
            # Parse grid configuration: dimensions and box requirements
            l = l.split()
            grid= tuple(int(x) for x in l[0][:-1].split('x'))
            bs = tuple(int(x) for x in l[1:])
            grids.append( (grid, bs))

# Part 1: Count grids where boxes can fit
c = 0
for i, g in enumerate(grids):
    # Total number of boxes needed
    nboxes = sum(*g[1:])
    # Maximum number of 3x3 boxes that can fit in grid
    pos_boxes = (g[0][0] // 3) * (g[0][1] // 3)
    
    if pos_boxes >= nboxes:
        # Grid has enough space for all boxes
        c += 1
        continue
    else:
        # Check if total filled cells exceeds grid area
        s = 0
        for j, b in enumerate(g[1]):
            s += sum(b*boxes[j])
        if s > g[0][0]*g[0][1]:
            # Not possible - too many cells
            continue
        else:
            # Needs detailed evaluation (not implemented)
            print (f"{i=} needs evaluation")

print("Part1:", c)


