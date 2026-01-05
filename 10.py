"""
Advent of Code 2025 - Day 10
Solve button/machine configuration problem using linear algebra.
Part 1: Brute force enumeration of button combinations.
Part 2: Solve system of linear equations for optimal button presses.
"""

from math import gcd
import itertools

# Read input from file
inp = open('10.txt').read().strip()

# Toggle for testing with example data
example = 0
if example:
    inp = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

inp = inp.strip().split('\n')

# Parse machine configurations
machines = []
for l in inp:
    l = l.split(" ")
    # Target state: which positions should be on (#) or off (.)
    target = l[0][1:-1]
    target = list(1 if c == "#" else 0 for c in target)
    # Button effects: which positions each button toggles
    buttons = []
    for item in l[1:-1]:
        item = tuple(int(x) for x in item[1:-1].split(","))
        buttons.append(item)
    # Jolt values: target number of toggles per position
    jolts = list(int(x) for x in l[-1][1:-1].split(","))

    machines.append( [ target, buttons, jolts ] )

def part1(machines):
    """
    Find minimum button presses to reach target using brute force.
    Try all possible combinations of button presses.
    
    Args:
        machines: List of machine configurations
    
    Returns:
        Sum of minimum button presses for all machines
    """
    s = 0
    for m in machines:
        buttons = m[1]
        nb = len(buttons)
        target = m[0]
    
        minc = 1e20
        # Try all combinations of pressing/not pressing each button
        for x in itertools.product(*[(0,1)]*nb):
            count = 0
            start = [0]*len(target)
            for i,v in enumerate(x):
                if v:
                    # Toggle positions affected by this button
                    for b in buttons[i]:
                        start[b] = 0 if start[b] else 1
                    count += 1
            if start == target:
                if count < minc:
                    minc = count
        s += minc
    return s

def print_matrix(A):
    """Helper function to print matrix (for debugging)."""
    for l in A:
        for c in l:
            #c = float(c)
            print(f"{c}", end=" ")
        print()
    print()


def not_zero(obj):
    """Check if value is non-zero (for numerical stability)."""
    return obj != 0
    return abs(obj) >1e-10

def is_zero(obj):
    """Check if value is zero."""
    return not not_zero(obj)

def is_integer(values):
    """Check if all values are close to integers."""
    for v in values:
        if abs(round(v) - v) > 1e-2:
            return False
    return True

def solve_gs(w, A, B, s):
    """
    Back-substitution to solve upper triangular system.
    
    Args:
        w: Machine index (for debugging)
        A: Coefficient matrix
        B: Target vector
        s: Solution vector (partially filled)
    
    Returns:
        Complete solution vector
    """
    n = len(B)
    for i in range(n-1,-1,-1):
        v = B[i]
        for j in range(n-1,i,-1):
            v -= s[j]*A[i][j]
        if not_zero(A[i][i]):
            s[i] = v/A[i][i]
    return s

def solve_matrix(w, A, B):
    """
    Solve system of linear equations Ax = B using Gaussian elimination.
    Uses integer arithmetic to maintain precision.
    
    Args:
        w: Machine index (for debugging)
        A: Coefficient matrix (may be non-square)
        B: Target vector
    
    Returns:
        Solution vector x
    """
    maxB = max(B)
    m = len(A)
    n = len(A[0])
    
    # Convert to square system if needed (least squares approach)
    if m != n:
        Am = [] 
        Bm = []
        for i in range(n):
            l = []
            for j in range(n):
                s = 0
                for k in range(m):
                    s += A[k][i]*A[k][j]
                l.append(s)
            Am.append(l)
            s = 0
            for k in range(m):
                s += A[k][i]*B[k]
            Bm.append(s)


        A = Am
        B = Bm

    # Gaussian elimination with row pivoting
    for i in range(n):
        # Find pivot
        for j in range(i, n):
            if not_zero(A[j][i]):
                if j != i:
                    A[j], A[i] = A[i],A[j]
                    B[j], B[i] = B[i],B[j]
                break
        if j == n:
            continue
        if is_zero(A[i][i]):
            continue
        # Eliminate below pivot
        for k in range(i+1,n):
            factor = A[k][i] #/A[i][i]
            for l in range(i,n):
                A[k][l] *= A[i][i]
                A[k][l] -= factor*A[i][l] 
            B[k] *= A[i][i]
            B[k] -= factor*B[i]

            # Reduce by GCD to keep numbers manageable
            g = gcd(B[k], *A[k])
            if g:
              for l in range(i,n):
                  A[k][l] //= g
              B[k] //= g

    # Back-substitution
    s = [None]*n
    invalid = []
    for i in range(n-1,-1,-1):
        v = B[i]
        for j in range(n-1,i,-1):
            v -= s[j]*A[i][j]
        if not_zero(A[i][i]):
            s[i] = v/A[i][i]
        else:
            # Underdetermined: try different values
            invalid.append(i)
            s[i] = 0

    if not invalid and min(s) < -1e-8:
        print(w, s)
        import pdb; pdb.set_trace()

    # Handle underdetermined system by trying combinations
    if invalid:
        options = [list(range(maxB+1))]*len(invalid)
        smin = 1e20
        for x in itertools.product(*options):
            s = [None]*n
            for iii, v in enumerate(x):
                s[invalid[iii]] = v

            ret = solve_gs(w, A, B, s)
            if min(ret) < -1e-7:
                continue
            if not is_integer(ret):
                continue

            sumr = sum(ret)
            if sumr < smin:
                smin = sumr
                ssaved = ret
        if smin < 1e20:
            s = ssaved

    if min(s) < -1e-8:
        print(w, s)
        import pdb; pdb.set_trace()
    s = [int(round(u)) for u in s]
    return s

def part2(machines):
    """
    Solve for exact button presses using linear algebra.
    Each button press affects specific positions, need to achieve target jolts.
    
    Args:
        machines: List of machine configurations
    
    Returns:
        Sum of total button presses for all machines
    """
    c = 0
    for w,m in enumerate(machines):
        # Build coefficient matrix: rows = positions, cols = buttons
        A = []
        for b in m[1]:
            l = [0]*len(m[-1])
            for v in b:
               l[v] = 1
            A.append(l)
        # Transpose to get positions as rows
        At = []
        for i in range(len(A[0])):
            l = []
            for j in range(len(A)):
                l.append(A[j][i])
            At.append(l)
        A = At
        B = m[-1][:]
        values = solve_matrix(w, A, B)
        if not is_integer(values):
            raise RuntimeError(f"Wrong values {values} for {w}")
        s = sum(values)
    
        # Verify solution
        jolts = [0]*len(m[-1])
        for en, v in enumerate(values):
            for b in m[1][en]:
                jolts[b] += int(round(v))
    
        if [x for x in jolts] != m[-1]:
            print(f"Value does not match for {w}, {jolts}, {values}, {m[-1]}")
        
        if (min(values) < 0):
            print(A,B)
            print(w, m, values, s)
            break
        c += s
    return c


print("Part1:", part1(machines))
print("Part2:", part2(machines))
      
