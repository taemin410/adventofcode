from itertools import combinations

from collections import deque

f = open("day9.input", "r+")

lines = [ (a.strip()) for a in f.readlines() ] 

disk = []
isFile = True
counter = 0
for i in lines[0]:
    
    if isFile:
        for j in range(int(i)):
            disk.append(str(counter)) 

        counter +=1 
        
        isFile = False
    else:
        for j in range(int(i)):
            disk.append( "." )
        isFile = True

newDisk = []
left = len(disk) - 1
for i in range(len(disk)):
    if left < i:
        break

    if disk[i] == '.': 
        while disk[left] == '.':
            left -= 1

        #print("appending ", disk[left])
        newDisk.append(disk[left])
        left -= 1
    else:
        #print("* appending ", disk[i])
        newDisk.append(disk[i])
        
checksum = 0
counter = 0
for a in newDisk[:-1]:
    checksum += int(a) * counter
    counter +=1
    
print(checksum)
