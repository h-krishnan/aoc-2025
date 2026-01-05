"""
Advent of Code 2025 - Day 9
Find largest rectangle inscribed in a polygon.
Part 1: Any rectangle aligned with axes.
Part 2: Rectangle that doesn't intersect polygon edges.
"""

# Read input from file
inp = open('9.txt').read().strip()

factor = 300  # Scaling factor for visualization

# Toggle for testing with example data
example = 0
if example:
    factor = 0.1
    inp = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""".strip()


inp = inp.split()

# Parse polygon vertices
tiles = []
for l in inp:
    x,y = l.split(',')
    tiles.append((int(x),int(y)))

def line_cuts_rectangle(tl, br, l1, l2):
    """
    Check if a line segment intersects with a rectangle's interior.
    
    Args:
        tl: Top-left corner of rectangle (x, y)
        br: Bottom-right corner of rectangle (x, y)
        l1: First endpoint of line segment (x, y)
        l2: Second endpoint of line segment (x, y)
    
    Returns:
        True if line cuts through rectangle, False otherwise
    """
    # Check vertical line segment
    if l1[0] == l2[0]:
        if l2[0] <= tl[0] or l2[0] >= br[0]:
            return False
        if l1[1] > l2[1]:
            l1,l2 = l2,l1
        if l2[1] <= tl[1] or l1[1] >= br[1]:
            return False
    # Check horizontal line segment
    elif l1[1] == l2[1]:
        if l2[1] <= tl[1] or l2[1] >= br[1]:
            return False
        if l1[0] > l2[0]:
            l1,l2 = l2,l1
        if l2[0] <= tl[0] or l1[0] >= br[0]:
            return False
    else:
        raise "OOPS!"
    return True

def valid_rect(t1,t2):
    """
    Check if a rectangle defined by two corners is valid (doesn't intersect polygon edges).
    
    Args:
        t1: First corner (x, y)
        t2: Second corner (x, y)
    
    Returns:
        True if rectangle is valid, False if it intersects edges
    """
    # Normalize rectangle to get top-left and bottom-right corners
    if t1[0] > t2[0]:
        if t1[1] > t2[1]:
            rect = [
                    (t2[0],t2[1]),
                    (t1[0],t1[1]),
                    ]
        else:
            rect = [
                    (t2[0],t1[1]),
                    (t1[0],t2[1]),
                    ]
    else:
        if t1[1] > t2[1]:
            rect = [
                    (t1[0],t2[1]),
                    (t2[0],t1[1]),
                    ]
        else:
            rect = [
                    (t1[0],t1[1]),
                    (t2[0],t2[1]),
                    ]
    # Check each polygon edge
    for i1 in range(len(tiles)-1):
        j1 = (i1+1)%len(tiles)
        if line_cuts_rectangle(rect[0], rect[1], tiles[i1], tiles[j1]):
            return False
    return True

def draw(rect = None):
    """
    Visualize polygon and optional rectangle using turtle graphics.
    
    Args:
        rect: Optional rectangle to draw in red (tuple of top-left, bottom-right)
    """
    import turtle
    t = turtle.Turtle()
    t.up()
    t.setpos((tiles[-1][0]/factor, tiles[-1][1]/factor))
    t.down()
    # Draw polygon
    for p in tiles:
        t.setpos((p[0]/factor, p[1]/factor))
    # Draw rectangle if provided
    if rect:
        tl,br = rect
        t.up()
        t.pencolor("red")
        t.setpos(tl[0]/factor, tl[1]/factor)
        t.down()
        t.setpos(tl[0]/factor, br[1]/factor)
        t.setpos(br[0]/factor, br[1]/factor)
        t.setpos(br[0]/factor, tl[1]/factor)
        t.setpos(tl[0]/factor, tl[1]/factor)
    turtle.mainloop()

def solve(part):
    """
    Find the largest rectangle.
    
    Part 1: Any rectangle between two vertices.
    Part 2: Rectangle that doesn't intersect polygon edges.
    
    Args:
        part: Problem part (1 or 2)
    
    Returns:
        Area of largest valid rectangle
    """
    global part2_sol
    m = 0  # Maximum area
    r = None  # Best rectangle
    # Try all pairs of vertices as opposite corners
    for i in range(len(tiles)):
        for j in range(i+1, len(tiles)):
            t1 = tiles[i]
            t2 = tiles[j]

            # Part 2: validate rectangle doesn't cut edges
            if part == 2 and not valid_rect(t1,t2):
                continue
    
            # Calculate area
            a = (abs(t1[0] - t2[0])+1)*(abs(t1[1]-t2[1])+1)
            if a > m:
                m = a
                r = t1,t2
                part2_sol = r
    return m
print("Part1:", solve(1))
print("Part2:", solve(2))

