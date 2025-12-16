inp = open('9.txt').read().strip()

factor = 300

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

tiles = []
for l in inp:
    x,y = l.split(',')
    tiles.append((int(x),int(y)))

def line_cuts_rectangle(tl, br, l1, l2):
    if l1[0] == l2[0]:
        if l2[0] <= tl[0] or l2[0] >= br[0]:
            return False
        if l1[1] > l2[1]:
            l1,l2 = l2,l1
        if l2[1] <= tl[1] or l1[1] >= br[1]:
            return False
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
   for i1 in range(len(tiles)-1):
       j1 = (i1+1)%len(tiles)
       if line_cuts_rectangle(rect[0], rect[1], tiles[i1], tiles[j1]):
           return False
   return True

def draw(rect = None):
  import turtle
  t = turtle.Turtle()
  t.up()
  t.setpos((tiles[-1][0]/factor, tiles[-1][1]/factor))
  t.down()
  for p in tiles:
      t.setpos((p[0]/factor, p[1]/factor))
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
    global part2_sol
    m = 0
    r = None
    for i in range(len(tiles)):
        for j in range(i+1, len(tiles)):
            t1 = tiles[i]
            t2 = tiles[j]

            if part == 2 and not valid_rect(t1,t2):
                continue
    
            a = (abs(t1[0] - t2[0])+1)*(abs(t1[1]-t2[1])+1)
            if a > m:
                m = a
                r = t1,t2
                part2_sol = r
    return m
print("Part1:", solve(1))
print("Part2:", solve(2))

