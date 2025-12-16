inp = open('8.txt').read()
nconnect = 1000

example = 0
if example:
    inp = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
    """
    nconnect = 10

inp = inp.strip()
inp = inp.split("\n")

def solve(inp):
    boxes = []
    part1 = None
    part2 = None
    
    for l in inp:
        l = tuple(int(x) for x in l.strip().split(','))
        boxes.append(l)
    
    distances = {}
    for b1 in boxes:
        for b2 in boxes:
            if b1 == b2: continue
            d = (b1[0]-b2[0])**2 + (b1[1]-b2[1])**2 + (b1[2]-b2[2])**2
            if (b2,b1) not in distances:
                distances[(b1,b2)] = d
    
    rev = [(v,k) for k,v in distances.items()]
    rev.sort(key=lambda x: x[0])
    
    cmap = {}
    c = 0
    nsets = len(boxes)
    for d,r in rev:
        c += 1
        if c == nconnect+1:
           circuits = list(set(tuple(x) for x in cmap.values()))
           circuits.sort(key=lambda x: -len(x))
           part1 = len(circuits[0])*len(circuits[1])*len(circuits[2])
    
        rc0 = cmap.get(r[0])
        rc1 = cmap.get(r[1])
        if rc0 and (rc0 == rc1):
            continue
        if rc0 and rc1:
            newc = rc0 | rc1
            for r1 in rc0:
                cmap[r1] = newc
            for r1 in rc1:
                cmap[r1] = newc
            nsets -= 1
        elif rc0:
            last = r
            rc0.add(r[1])
            cmap[r[1]] = rc0
            nsets -= 1
        elif rc1:
            last = r
            rc1.add(r[0])
            cmap[r[0]] = rc1
            nsets -= 1
        else:
            last = r
            newc = set()
            newc.add(r[0])
            newc.add(r[1])
            cmap[r[0]] = newc
            cmap[r[1]] = newc
            nsets -= 1
    
        if nsets == 1:
            part2 = r[0][0]*r[1][0]
            break
    return part1, part2

part1,part2 = solve(inp)
print("Part1:", part1)
print("Part2:", part2)
    
