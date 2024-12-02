
def read_input_from_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.readlines()


lines = read_input_from_file("day2/input.txt")

def check_increase(nums):
    for i in range(len(nums) - 1):

        diff = nums[i+1] - nums[i]

        if diff < 1: 
            # meaning negative or zero
            return False
        elif diff > 3:
            return False

    return True


def check_decrease(nums):
    for i in range(len(nums) - 1):

        diff = nums[i] - nums[i+1]

        if diff < 1: 
            # meaning negative or zero
            return False
        elif diff > 3:
            return False

    return True

def check_is_safe(numbers):
    is_safe = False
    is_increase = (numbers[1] - numbers[0]) > 0
            
    if is_increase:
        is_safe = check_increase(numbers)
    else:
        is_safe = check_decrease(numbers)

    return is_safe


safety = 0
for line in lines:
    numbers = [ int(x) for x in line.split()] # gives numbers in order
    
    if check_is_safe(numbers):
        safety+=1 
    else:

        # get modified list without one element at a time
        for i in range(len(numbers)):
            modified_li = numbers[:i] + numbers[i+1:]

            if check_is_safe(modified_li):
                safety+=1 
                break
                


print(safety)
