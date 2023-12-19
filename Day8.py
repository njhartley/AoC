import numpy as np
from typing import List, Tuple

# Open the file and read the lines into a list
lines: List[str] = open("./Input/Day8.txt").read().splitlines()

# Open file as iterable
#f = open("./Input/Day8.txt")

labels = []
right = []
left= []

## Get three lists of data (lab,L,R)
for i,line in enumerate(lines[2:]):
    lab,_,rlab,llab = line.split()
    labels.append(lab)
    left.append(rlab[1:-1])
    right.append(llab[:-1])

## Get commands
command = lines[0]
ncom = len(command)

## Part 2
## Get starting positions
pos0 = []
for lab in labels:
    if lab[-1]=='A':
        pos0.append(lab)


def test(arr):
    for p in arr:
        if p!='Z':
            return 1
    return 0

rv = []

for pos in pos0:
    com=0
    while pos[-1]!='Z':
        ipos = labels.index(pos)
        dirn = command[com%ncom]
        #print(pos,ipos,com,dirn)
        
        com += 1
        if dirn=='R':
            pos = right[ipos]
        elif dirn=='L':
            pos = left[ipos]
        else:
            print("You've fucked up")
    print("position %s, %d steps"%(pos,com))
    rv.append(com)

v1 = int(rv[0]*rv[1]/(np.gcd(rv[0],rv[1])))
print(rv[0],rv[1],v1)
v2 = int(rv[2]*rv[3]/(np.gcd(rv[2],rv[3])))
print(rv[2],rv[3],v2)
v3 = int(rv[4]*rv[5]/(np.gcd(rv[4],rv[5])))
print(rv[4],rv[5],v3)

v11= int(v1*v2 / (np.gcd(v1,v2)))
print(v1,v2,v11)

run_prod= int(v3 * v11 / (np.gcd(v3,v11)))
print(v3,v11,run_prod)

print("%d steps"%run_prod)
        

## Part 1
##pos = 'AAA'
##com = 0
##
##while pos!='ZZZ':
##    ipos = labels.index(pos)
##    dirn = command[com%ncom]
##    #print(pos,ipos,com,dirn)
##    
##    com += 1
##    if dirn=='R':
##        pos = right[ipos]
##    elif dirn=='L':
##        pos = left[ipos]
##    else:
##        print("You've fucked up")
##print("%d steps"%com)
    

