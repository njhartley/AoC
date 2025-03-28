import numpy as np
from typing import List, Tuple

# Open the file and read the lines into a list
lines: List[str] = open("./Input/Day10.txt").read().splitlines()

# Open file as iterable
#f = open("./Input/Day5.txt")

for i,line in enumerate(lines):
    try:
        ind = line.index('S')
        print(lines[i-1][ind-1:ind+2])
        print(lines[i][ind-1:ind+2])
        print(lines[i+1][ind-1:ind+2])
        print(i,ind)
        break
    except:
        pass

pos_y0 = i
pos_x0 = ind

dx0 = 0
dy0 = 1

pos_x = pos_x0 + dx0
pos_y = pos_y0 + dy0

steps=1
loop = [(pos_y0,pos_x0)]

while pos_x!=pos_x0 or pos_y!=pos_y0:
#for i in range(10):
    ## Get pipe value
    pipe = lines[pos_y][pos_x]

    # Find new progress
    if pipe=='F' or pipe=='J':
        dx1 = -dy0
        dy1 = -dx0
    elif pipe=='L' or pipe =='7':
        dx1 = dy0
        dy1 = dx0
    elif pipe=='|' or '-':
        dx1 = dx0
        dy1 = dy0
    else:
        print("It's a %s"%pipe)

    loop.append((pos_y,pos_x))
    #print(pipe, pos_y, pos_x)

    pos_x = pos_x + dx1
    pos_y = pos_y + dy1

    dx0 = dx1
    dy0 = dy1

    steps += 1

print("Steps for loop: %d"%steps)
print("Greatset distance: %d"%(steps/2))

tot_area = 0

for i in range(len(lines)):
    in_area = False
    for j in range(len(lines[0])):     
        try:
            coord = (i,j)
            loop.index(coord)
            if lines[i][j] in ['7','F','|','S']:
                in_area=not(in_area)
            #print(i,j,lines[i][j],in_area,1)
        except:
            tot_area += int(in_area)
            #if in_area:
            #    print(i,j)
            #print(i,j,lines[i][j],in_area,0)
        
print(tot_area)
        

    
        




