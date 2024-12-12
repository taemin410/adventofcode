from itertools import combinations

from collections import deque, defaultdict

f = open("day12.test", "r+")

lines = [ list(a.strip()) for a in f.readlines() ] 

print(lines)

max_x = len(lines[0])
max_y = len(lines)
SEEN = set()
perimeters = defaultdict(int)
spaces = defaultdict(int)

sum = 0
def bfs(x, y, m):
    
    global sum

    to_search = deque()
    X = set()
    Y = set()
    PERIM = dict()
    adjacent = defaultdict(set)

    if (x,y) not in SEEN:
        to_search.append((x,y))
        alphabet = m[y][x]
    else:
        return

    while len(to_search) != 0:

        dx, dy = to_search.popleft()
        if (dx, dy) in SEEN:
            continue
#        print("from: ", dx, dy)
        SEEN.add((dx, dy))
        X.add(dx)
        Y.add(dx)

        left  = dx - 1 
        right = dx + 1 
        up    = dy - 1 
        down  = dy + 1 

        spaces[alphabet] +=1
        peri = 0
        four_directions = [(dy, left), (dy, right), (up, dx), (down, dx)]
        for pos_y, pos_x in four_directions:
            if pos_x != -1 and pos_x != max_x and pos_y != -1 and pos_y != max_y:
                if m[pos_y][pos_x] is alphabet:
                    if (pos_x, pos_y) not in SEEN:
                        to_search.append((pos_x, pos_y))
                else:
                    peri +=1
            else:
                peri += 1

        perimeters[alphabet] += peri

    sides = 0
    for k, v in adjacent.items():
        SEEN_ADJ = set()
        for r, c in v: # adjecent alphabets
            if (r, c) not in SEEN_ADJ:
                sides += 1
                Q = deque([(r, c)])
                while len(Q) != 0:
                    r2, c2 = Q.popleft()
                    if (r2, c2) in SEEN_ADJ:
                        continue
                    SEEN_ADJ.add((r2,c2))
                    for (dr, dc) in [(-1,0),(0,1),(1,0),(0,-1)]:
                        rr, cc = r2 + dr, c2 + dc
                        if (rr, cc) in v:
                            Q.append((rr,cc))

            


    print(spaces[alphabet], sides)
    sum += spaces[alphabet] * sides
    spaces[alphabet] = 0 
    perimeters[alphabet] = 0

        
                    
#
#            
#for i in range(max_x):
#    for j in range(max_y):
#        if lines[j][i] == 0:
#            bfs(i, j, lines)
#
#print(sum)

            
for i in range(len(lines[0])):
    for j in range(len(lines)):
        bfs(i, j, lines)


print(sum)
