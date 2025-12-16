inp = open('2.txt').read()

example = 0
if example:
    inp = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
"""
inp = inp.strip().split(",")

def solve(inp, part):
    t = 0
    for l in inp:
        i1, i2 = [int(x) for x in l.split("-")]
        for x in range(max(i1, 10), i2+1):
            s = str(x)
            if part == 1:
                if len(s) % 2 != 0:
                    continue
                if s[:len(s)//2] == s[len(s)//2:]:
                    t += x
            else:
                start = 1 if part == 2 else len(s)//2
                for i in range(start, len(s)//2 + 1):
                    s1 = s[:i]*(len(s)//i)
                    if s == s1:
                        t += x
                        break
    return t

print("Part 1:", solve(inp, 1))
print("Part 2:", solve(inp, 2))

