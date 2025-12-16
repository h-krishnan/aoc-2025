inp = open('5.txt').read()

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
    count = 0
    for i in ids:
        for r in ranges:
            if i >= r[0] and i <= r[1]:
                count += 1
                break
    return count


def part2():
    lst = [(r[0],1) for r in ranges] + [(r[1],-1) for r in ranges]
    lst.sort(key = lambda x: x[0])

    count = 0
    depth = 0
    curr = 0
    for l,s in lst:
        if s == -1:
            depth -= 1
            if depth == 0:
                count += l - curr + 1
        elif s == 1:
            depth += 1
            if depth == 1:
                curr = l
    return count

print("Part1:", part1())
print("Part2:", part2())

        


