from itertools import combinations

from collections import deque, defaultdict
import numpy as np

f = open("day13.input", "r+")

lines = [ a.strip() for a in f.readlines() ] 

#print(lines)



sum = 0
n = []
for line in lines:
    if line.startswith("Button"):
        aorb = line.split(' ')[1][0]
        #print(aorb)
        numbers = line.split(":")[1]
        #print(numbers)
        x = int(numbers.split(",")[0].split("+")[-1])
        y = int(numbers.split(",")[1].split("+")[-1])
        #print(x, y)

        n.append((x,y))
            
    elif line.startswith("Prize"):
        numbers = line.split(":")[1]

        target_x = int(numbers.split(",")[0].split("=")[-1])
        target_y = int(numbers.split(",")[1].split("=")[-1])
        #print(target_x, target_y)

            
        eq = [] 
        A = [[],[]]
        B = []
        for dx, dy in n:
            newa = dx + dy
            A[0].append(dx)
            A[1].append(dy)
            #eq.append(newa)
        B.append(target_x)
        B.append(target_y)

            
        #print(A)
        #print(B)
        res = np.linalg.inv(A).dot(B)

        if np.all(np.mod(res, 1) == 0):
            print(res)
            res = res.astype(int)
            sum += res[0]*3 + res[1]
            

    else:
        n.clear()

print(sum)
