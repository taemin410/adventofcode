
import regex as re
import numpy as np

# a)

file = open('day4/input.test', 'r')
content = file.read().split('\n')
content = np.array([list(c) for c in content])

count = 0

rows = len(content)
cols = len(content[0])

# rows
for i in range(rows):
    list_row = content[i, :]
    list_str = "".join(list_row)
    count += len(re.findall("XMAS|SAMX", list_str, overlapped=True))

# columns
for j in range(cols):
    list_row = content[:, j]
    list_str = "".join(list_row)
    count += len(re.findall("XMAS|SAMX", list_str, overlapped=True))

# diagonals
for k in range(-(cols-1), cols):
    a = "".join(np.diag(content, k))
    b = "".join(np.diag(np.flipud(content), k))
    count += len(re.findall("XMAS|SAMX", a, overlapped=True)) + len(re.findall("XMAS|SAMX", b, overlapped=True))

print(count)

# b)

file = open('input_day4.txt', 'r')
content = file.read().split('\n')
content = np.array([list(c) for c in content])

rows = len(content)
cols = len(content[0])

count = 0
for i in range(1, rows-1):
    for j in range(1, rows-1):
        if content[i, j] == 'A':
            count += int( 
                (content[i-1, j-1] == 'M' and content[i+1, j+1] == 'S' or \
                content[i-1, j-1] == 'S' and content[i+1, j+1] == 'M') and \
                (content[i+1, j-1] == 'M' and content[i-1, j+1] == 'S' or \
                content[i+1, j-1] == 'S' and content[i-1, j+1] == 'M')
            )

print(count)
