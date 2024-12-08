from itertools import combinations

from collections import deque

f = open("day8.input", "r+")

lines = [ list(a.strip()) for a in f.readlines() ] 

class Position:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f"{self.x},{self.y}"

    def __repr__(self):
        return f"({self.x},{self.y})"

def calculate_x_y_distance(pos1, pos2):
    
    x_distance = pos1.x - pos2.x
    y_distance = pos1.y - pos2.y

    return x_distance, y_distance


def is_valid_pos(pos, max_x, max_y ):
    return (pos.x < max_x and 0 <= pos.x) and (pos.y < max_y and 0 <= pos.y)


uniq = []
for j in lines:
    for i in j:
        if i != '.' and i not in uniq:
            uniq.append(i)

uniq_dict = dict()

for uniq_char in uniq:
    uniq_dict[uniq_char] = []

max_x = len(lines[0])
max_y = len(lines)
for x in range(max_x):
    for y in range(max_y):
        if lines[y][x] in uniq:
            pos = Position(x, y)
            #print(lines[y][x], x, y)
            uniq_dict[lines[y][x]].append(pos)


sum = 0

res = set() 
def do_calc(points):
    global sum
    combination_list = list(combinations(points, 2))

    for c in combination_list:

        for i in range(0, max_x):
        
            x, y = calculate_x_y_distance(c[0], c[1])

                
            x = x * i
            y = y * i

            candidate_antenna_1 =  Position(c[0].x + x, c[0].y + y)
            candidate_antenna_2 =  Position(c[1].x - x, c[1].y - y)

            #print(candidate_antenna_1, candidate_antenna_2)
            
            if is_valid_pos(candidate_antenna_1, max_x, max_y):
                x_pos, y_pos = candidate_antenna_1.x, candidate_antenna_1.y
                if lines[y_pos][x_pos] == '.':
                    lines[y_pos][x_pos] = '#'
                res.add((x_pos, y_pos))
                
            if is_valid_pos(candidate_antenna_2, max_x, max_y):
                x_pos, y_pos = candidate_antenna_2.x, candidate_antenna_2.y
                if lines[y_pos][x_pos] == '.':
                    lines[y_pos][x_pos] = '#'
                res.add((x_pos, y_pos))
            
            
for x in uniq_dict:
    do_calc(uniq_dict[x])

print(len(res))
