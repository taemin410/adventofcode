
def read_input_from_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.readlines()


lines = read_input_from_file("day1/input.txt")

left_list = []
right_list = []

for line in lines:
    left, right = line.split()
    left = int(left)
    right = int(right)

    left_list.append(left)
    right_list.append(right)



left_list.sort()
right_list.sort()

sum = 0
assert(len(left_list) == len(right_list))
for i in range(len(left_list)):
    diff = abs(left_list[i] - right_list[i])
    sum += diff
    
print(sum)

