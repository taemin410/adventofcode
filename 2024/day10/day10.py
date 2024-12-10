from itertools import combinations

from collections import deque

f = open("day10.input", "r+")

lines = [ list(a.strip()) for a in f.readlines() ] 
l = []
for line in lines:
    a = [] 
    for c in line: 
        if c == '.':
            a.append(None)
        else:
            a.append(int(c))
    l.append(a)

lines = l

for i in lines:
    print(i)

max_x = len(lines[0])
max_y = len(lines)
sum = 0

#def bfs(x, y, m):
#    global sum
#    
#    to_search = deque()
#    uniq = set()
#    assert(m[y][x] == 0)
#    START = 0
#
#    to_search.append((x,y, START))
#
#    while len(to_search) != 0:
#
#        dx, dy, num = to_search.popleft()
#        #print("from: ", dx, dy)
#
#        left  = dx - 1 
#        right = dx + 1 
#        up    = dy - 1 
#        down  = dy + 1 
#
#        # insert next candidates if expected num is there
#        if left != -1 and m[dy][left] == (num + 1):
#            if (num + 1) == 9:
#                uniq.add((left,dy))
#            else:
#                to_search.append((left, dy, (num + 1)))
#        if right != max_x and m[dy][right] == (num + 1):
#            if (num + 1) == 9:
#                uniq.add((right,dy))
#            else:
#                to_search.append((right, dy, (num + 1)))
#        if up != -1 and m[up][dx] == (num + 1):
#            if (num + 1) == 9:
#                uniq.add((dx,up))
#            else:
#                to_search.append((dx, up, (num + 1)))
#        if down != max_y and m[down][dx] == (num + 1):
#            if (num + 1) == 9:
#                uniq.add((dx,down))
#            else:
#                to_search.append((dx, down, (num + 1)))
#           
#
#    sum += len(uniq)
#
#            
#for i in range(max_x):
#    for j in range(max_y):
#        if lines[j][i] == 0:
#            bfs(i, j, lines)
#
#print(sum)

def bfs(x, y, m):
    global sum
    
    to_search = deque()
    assert(m[y][x] == 0)
    START = 0

    to_search.append((x,y, START))

    while len(to_search) != 0:

        dx, dy, num = to_search.popleft()
        print("from: ", dx, dy)

        left  = dx - 1 
        right = dx + 1 
        up    = dy - 1 
        down  = dy + 1 

        # insert next candidates if expected num is there
        if left != -1 and m[dy][left] == (num + 1):
            if (num + 1) == 9:
                sum += 1
                print("sum here: ", sum)
            else:
                to_search.append((left, dy, (num + 1)))
        if right != max_x and m[dy][right] == (num + 1):
            #print(right, dy, (num + 1))
            if (num + 1) == 9:
                sum += 1
                print("sum here: ", sum)
            else:
                to_search.append((right, dy, (num + 1)))
        if up != -1 and m[up][dx] == (num + 1):
            #print(dx, up, (num + 1))
            if (num + 1) == 9:
                sum += 1
                print("sum here: ", sum)
            else:
                to_search.append((dx, up, (num + 1)))
        if down != max_y and m[down][dx] == (num + 1):
            #print(dx, down, (num + 1))
            if (num + 1) == 9:
                sum += 1
                print("sum here: ", sum)
            else:
                to_search.append((dx, down, (num + 1)))
           


            
for i in range(max_x):
    for j in range(max_y):
        if lines[j][i] == 0:
            print(i, j)
            bfs(i, j, lines)

print(sum)
