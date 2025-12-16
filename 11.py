import functools
import time

inp = open('11.txt').read().strip()

inp = inp.strip().split('\n')

devices = {}
for l in inp:
    l = l.strip().split()
    s = l[0][:-1]
    devices[s] = l[1:]

@functools.cache
def connection_count(source, target):
    return 1 if source == target else \
            sum(connection_count(v, target)
                for v in devices.get(source, []))

def part1():
    return connection_count('you', 'out')

def part2():
    a = connection_count('svr', 'dac')
    if a:
        b = connection_count('dac', 'fft')
        if b:
            c = connection_count('fft', 'out')
            if c:
                 return a*b*c
    d = connection_count('svr', 'fft')
    e = connection_count('fft', 'dac')
    f = connection_count('dac', 'out')

    return d*e*f

print("Part1:", part1())
print("Part2:", part2())





