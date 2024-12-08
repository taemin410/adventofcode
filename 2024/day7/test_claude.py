
def concatenate(a, b):
    return int(str(a) + str(b))

def evaluate(nums, ops):
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            result += nums[i + 1]
        elif ops[i] == '*':
            result *= nums[i + 1]
        else:  # '||'
            result = concatenate(result, nums[i + 1])
    return result

def can_make_value(test_value, nums):
    n = len(nums) - 1  # number of operators needed
    # Try all possible combinations of +, *, and ||
    for i in range(3 ** n):  # Now we have 3 operators
        ops = deque()
        temp = i
        # Convert to base-3, each digit represents + (0), * (1), or || (2)
        for _ in range(n):
            op_type = temp % 3
            if op_type == 0:
                ops.append('+')
            elif op_type == 1:
                ops.append('*')
            else:
                ops.append('||')
            temp //= 3
        try:
            if evaluate(nums, ops) == test_value:
                return True
        except:
            continue
    return False


def solve(input_text):
    total = 0
    
    for line in input_text.strip().split('\n'):
        test_value, nums_str = line.split(': ')
        test_value = int(test_value)
        nums = [int(x) for x in nums_str.split()]
        
        if can_make_value(test_value, nums):
            total += test_value
            
    return total

# Read from file
with open('day7.input', 'r') as file:
    input_text = file.read()

print(solve(input_text))

