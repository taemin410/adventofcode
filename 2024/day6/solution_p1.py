
import numpy as np


f = open("day6.input", "r+")

lines = [ list(a.strip()) for a in f.readlines() ] 


m = np.array(lines)
# print(m)

v = np.zeros((len(lines), len(lines[0])))


# print(np.argwhere(m == '^'))
pos = np.argwhere(m == '^')[0]
x, y = pos[0], pos[1]
# print(np.argwhere(m == '^' || m == 'v' || m == '>' || m == '<'))

def check_bounds(x, y, m):
    #print( len(m[0]) , x ,  len(m) , y)
    if len(m) <= x or len(m[0]) <= y:
        return False
    elif 0 > x or 0 > y:
        return False
    return True

def check_blocker(x, y, m):
    #print("CHECK BLOKCER")
    if m[x][y] == '#':
        return False
    else:
        return True

def move(x, y, m, v):
    
    #print(x, y, m[x][y])
    if m[x][y] == '^':
        #print("UP")
        # move up
        v[x][y] = 1
        if not check_bounds(x-1,y,m):
            # print("OUTOFBOUNDS")
            return False, x, y, m, v
        if check_blocker(x-1, y, m):
            #print("NO BLOCKER")
            m[x][y] = '.'
            x -= 1
            m[x][y] = '^'
        else:
            # turn right
            #print("BLOCKER TURN RIGHT")
            m[x][y] = '>'
    elif m[x][y] == 'v':
        # move down
        v[x][y] = 1
        if not check_bounds(x+1,y,m):
            return False, x, y, m, v
        if check_blocker(x+1, y, m):
            m[x][y] = '.'
            x += 1
            m[x][y] = 'v'
        else:
            # turn right
            m[x][y] = '<'

    elif m[x][y] == '>':
        #print("RIGHT?")
        # move right
        v[x][y] = 1
        if not check_bounds(x,y+1,m):
            return False, x, y, m, v
        if check_blocker(x, y+1, m):
            m[x][y] = '.'
            y += 1
            m[x][y] = '>'
        else:
            # turn right
            m[x][y] = 'v'

    elif m[x][y] == '<':
        # move left
        v[x][y] = 1
        if not check_bounds(x,y-1,m):
            return False, x, y, m, v
        if check_blocker(x, y-1, m):
            m[x][y] = '.'
            y -= 1
            m[x][y] = '<'
        else:
            # turn right
            m[x][y] = '^'

    # print("END OF MOVE: ", x,y, m)
    # input("Next")
    return True, x, y, m, v


infinite = 0
for i in range(len(m)):
    for j in range(len(m[0])):

        init_pane = m.copy()
        #print(i, j)
        if init_pane[i][j] == '.':
            init_pane[i][j] = '#'
            #print("did swpa work?", init_pane)
        
            x, y = pos[0], pos[1]
            moving = True
            count = 0
            while moving:
                moving, x, y, init_pane, v = move(x,y,init_pane,v)
                if v[x][y] == 1:
                    infinite +=1
                    break
                #count+=1
                #if count == 10000:
                    ##print(init_pane)
                    #print("breaking")
                    #infinite +=1
                    #break

            # return to original
            init_pane[i][j] = '.'
            #print("AFTERWARDS")
            #print(init_pane)
        
            #input("NEXT")

print(infinite)

