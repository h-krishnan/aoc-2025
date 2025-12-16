inp = open('4.txt').read()

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

inp = inp.strip().split()

rolls = set()
for i, l in enumerate(inp):
    for j, c in enumerate(l.strip()):
        if c == '@':
            rolls.add((i, j))
        elif c == '.':
            pass
        else:
            print (f"Wrong {c} at {i},{j}")

maxx = len(inp[0])
maxy = len(inp)

def solve(rolls, part):
    count = 0
    while True:
        movable = set()
        for i in range(maxy):
            for j in range(maxx):
                if (i,j) in rolls:
                    c1 = 0
                    for (ii, jj) in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                        if (i+ii, j+jj) in rolls:
                            c1 += 1
                    if c1 < 4:
                        count += 1
                        movable.add((i,j))
        if not movable:
            break
        rolls -= movable
        movable.clear()
        if part == 1:
            break
    return count

def print_rolls():
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
    
