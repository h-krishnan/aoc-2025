inp = open('1.txt').read()

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

inp = inp.strip()
inp = inp.split('\n')

def part1(inp):
    d = 50
    c = 0
    for l in inp:
        i = l[0]
        n = int(l[1:])
        if i == 'R':
            d = (d + n) % 100
        else:
            d = (d - n) % 100
        if d == 0:
            c += 1
    return c


def part2(inp):
    d = 50
    c = 0
    for l in inp:
        i = l[0]
        n = int(l[1:])
        if n == 0:
            continue
        if i == 'R':
            d = (d + n)
            if d >= 100:
                c += d // 100
                d %= 100
        else:
            d = (d - n)
            if d <= 0:
                c += -d // 100
                if d+n != 0:
                    c += 1
            d %= 100
    return c

print (f"Part1: {part1(inp)}")
print (f"Part2: {part2(inp)}")
