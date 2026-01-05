"""
Advent of Code 2025 - Day 8
3D point clustering problem using minimum spanning tree approach.
Part 1: Find product of 3 largest clusters after N connections.
Part 2: Find when all points form one cluster.
"""

# Read input from file
inp = open('8.txt').read()
nconnect = 1000  # Number of connections for part 1

# Toggle for testing with example data
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
    """
    Build minimum spanning tree by connecting closest points.
    Track cluster formation at different connection counts.
    
    Args:
        inp: List of coordinate strings (x,y,z format)
    
    Returns:
        Tuple of (part1_answer, part2_answer)
    """
    boxes = []
    part1 = None
    part2 = None
    
    # Parse 3D coordinates
    for l in inp:
        l = tuple(int(x) for x in l.strip().split(','))
        boxes.append(l)
    
    # Calculate squared Euclidean distance between all pairs
    distances = {}
    for b1 in boxes:
        for b2 in boxes:
            if b1 == b2: continue
            d = (b1[0]-b2[0])**2 + (b1[1]-b2[1])**2 + (b1[2]-b2[2])**2
            if (b2,b1) not in distances:
                distances[(b1,b2)] = d
    
    # Sort edges by distance (for minimum spanning tree)
    rev = [(v,k) for k,v in distances.items()]
    rev.sort(key=lambda x: x[0])
    
    # Union-find data structure using sets
    cmap = {}  # Maps point to its cluster set
    c = 0      # Connection count
    nsets = len(boxes)  # Number of separate clusters
    
    for d,r in rev:
        c += 1
        # After nconnect connections, compute part 1 answer
        if c == nconnect+1:
           circuits = list(set(tuple(x) for x in cmap.values()))
           circuits.sort(key=lambda x: -len(x))
           part1 = len(circuits[0])*len(circuits[1])*len(circuits[2])
    
        rc0 = cmap.get(r[0])
        rc1 = cmap.get(r[1])
        
        # Skip if already in same cluster
        if rc0 and (rc0 == rc1):
            continue
        
        # Merge two existing clusters
        if rc0 and rc1:
            newc = rc0 | rc1
            for r1 in rc0:
                cmap[r1] = newc
            for r1 in rc1:
                cmap[r1] = newc
            nsets -= 1
        # Add to existing cluster
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
        # Create new cluster
        else:
            last = r
            newc = set()
            newc.add(r[0])
            newc.add(r[1])
            cmap[r[0]] = newc
            cmap[r[1]] = newc
            nsets -= 1
    
        # When all points form one cluster
        if nsets == 1:
            part2 = r[0][0]*r[1][0]
            break
    return part1, part2

part1,part2 = solve(inp)
print("Part1:", part1)
print("Part2:", part2)
    
