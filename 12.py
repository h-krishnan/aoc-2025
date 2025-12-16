import math
import itertools
import functools
import time

inp = open('12.txt').read().strip()

inp = inp.split('\n')

boxes = {}

grids = []

for i in range(len(inp)):
    l = inp[i].strip()
    if ':' in l:
        if 'x' not in l:
            bn = int(l[:-1])
            p = [0]*9
            for k in range(3):
                i = i+1
                for j,c in enumerate(inp[i].strip()):
                    if c == '#':
                        p[k*3 + j] = 1
            boxes[bn] = p
        else:
            l = l.split()
            grid= tuple(int(x) for x in l[0][:-1].split('x'))
            bs = tuple(int(x) for x in l[1:])
            grids.append( (grid, bs))

c = 0
for i, g in enumerate(grids):
    nboxes = sum(*g[1:])
    pos_boxes = (g[0][0] // 3) * (g[0][1] // 3)
    if pos_boxes >= nboxes:
        c += 1
        continue
    else:
        s = 0
        for j, b in enumerate(g[1]):
            s += sum(b*boxes[j])
        if s > g[0][0]*g[0][1]:
            continue # not possible
        else:
            print (f"{i=} needs evaluation")

print("Part1:", c)


