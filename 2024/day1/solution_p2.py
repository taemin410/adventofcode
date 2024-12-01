
from collections import defaultdict

def read_input_from_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.readlines()


lines = read_input_from_file("day1/input_p1.txt")

left_list = []
right_dir = defaultdict(int)

def increment_key(key):
    right_dir[key] += 1

for line in lines:
    left, right = line.split()
    # left = int(left)
    right = int(right)

    # left_list.append(left)
    increment_key(right)

sum = 0
for line in lines:
    left, right = line.split()
    left = int(left)

    sum += left * right_dir[left]

print(sum)

