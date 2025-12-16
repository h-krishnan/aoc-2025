inp = open('3.txt').read()

example = 0
if example:
    inp = """
987654321111111
811111111111119
234234234234278
818181911112111
"""

inp = inp.strip().split('\n')

def find_n_digits(string, n):
    if len(string) == n:
        return int(string)
    mx = 0
    ld = 0
    for c in range(len(string)-n+1):
        if int(string[c]) > mx:
            mx = int(string[c])
            ld = c
    if n == 1:
        v = mx
    else:
        v = 10**(n-1)*mx + find_n_digits(string[ld+1:], n-1)
    return v

def part1(inp):
    s = 0
    for l in inp:
        s += find_n_digits(l.strip(), 2)
    return s

def part2(inp):
    s = 0
    for l in inp:
        s += find_n_digits(l.strip(), 12)
    return s

print("Part 1:", part1(inp))
print("Part 2:", part2(inp))
