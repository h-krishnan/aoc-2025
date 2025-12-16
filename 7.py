inp = open('7.txt').read()

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

beams = set()
splitters = set()

for i,l in enumerate(inp):
    for j, c in enumerate(l.strip()):
        if c == 'S':
            beams.add((i,j))
        elif c == '^':
            splitters.add((i,j))

imax = i
jmax = j

def print_beams():
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

all_beams = set()
all_beams |= beams
splits = 0
p = 1
while True:
    if p > imax:
        break
    p += 1
    beams = set((i,j) for i,j in beams)
    new_beams = set()
    for i,j in beams:
        if (i+1,j) in splitters:
            splits += 1
            if j > 0:
                new_beams.add((i+1,j-1))
            if j < jmax:
                new_beams.add((i+1,j+1))
        else:
            new_beams.add((i+1,j))
    beams = new_beams
    all_beams |= beams

print("Part1:", splits)


import functools
@functools.cache
def n_ways(beam):
    i, j = beam
    if i == 0:
        return 1
    s = 0
    if (i-1, j) in all_beams:
        s += n_ways((i-1,j))

    if (i,j-1) in splitters and (i-1,j-1) in all_beams:
        s += n_ways((i-1,j-1))
    if (i,j+1) in splitters and (i-1,j+1) in all_beams:
        s += n_ways((i-1,j+1))
    return s

beams = sorted(beams, key=lambda x:x[1])
s= 0
for b in beams:
    n = n_ways(b)
    s += n

print("Part2:", s)
