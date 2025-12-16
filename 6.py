inp = open('6.txt').read()

example = 0
if example:
    inp = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +"""

def compute_value(data, oplist):
    s = 0
    for d, op in zip(data, oplist):
        if op == '*':
            v = 1
            for x in d:
                v *= x
            s += v
        elif op == '+':
            s += sum(d)
        else:
            print("Unvalid op", op)
    return s

def part1(inp):
    inp = inp.strip().split('\n')
    data = list(list() for i in inp[0])
    for l in inp[:-1]:
        l = [int(x) for x in l.strip().split()]
        for d,i in zip(data, l):
            d.append(i)
    return compute_value(data, inp[-1].strip().split())


def part2(inp):
    inp = inp.strip().split('\n')
    data = list(list() for i in inp[0])
    inp1 = ["" for c in inp[0]]
    for l in inp[:-1]:
        for i, c in enumerate(l):
            inp1[i] = inp1[i] + c

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

