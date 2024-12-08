
from collections import deque

f = open("day7.input", "r+")

lines = [ a.strip() for a in f.readlines() ] 

def operation_concat(a, b):
    base10 = len(str(b))
    res = a * (10 ** base10) + b 
    return res
    

sum = 0
for line in lines:
    
    numbers = line.split(":")
    result = int(numbers[0])

    operands = [ int(i) for i in numbers[1].strip().split(" ")] 


    queue = deque()

    x = 0
    queue.append((operands[x], x))
    while len(queue) > 0: 
        
        ans, pos = queue.popleft()
        if pos + 1 == len(operands):
            #print(ans)
            if ans == result:
                sum += ans
                break
        elif ans <= result:
            # print(ans, operands[pos])
            queue.append((ans + operands[pos+1], pos+1))
            queue.append((ans * operands[pos+1], pos+1))
            queue.append((operation_concat(ans,operands[pos+1]), pos+1))


print(sum)
    

    




