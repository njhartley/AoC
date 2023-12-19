import numpy as np
import re

f = open("./Day5 Input.dat")

for i in range(10):
    next(f)
#lines = f.readlines()

# Define empty dictionary
stacks = {}

stacks[1] = ['F','C','J','P','H','T','W']
stacks[2] = ['G','R','V','F','Z','J','B','H']
stacks[3] = ['H','P','T','R']
stacks[4] = ['Z','S','N','P','H','T']
stacks[5] = ['N','V','F','Z','H','J','C','D']
stacks[6] = ['P','M','G','F','W','D','Z']
stacks[7] = ['M','V','Z','W','S','J','D','P']
stacks[8] = ['N','D','S']
stacks[9] = ['D','Z','S','F','M']


for a in stacks:
    print(a,stacks[a])


for line in f:
    _,num,_,i_from,_,i_to = line.split()
    num = int(num); i_from=int(i_from); i_to=int(i_to)

    stacks[i_to].extend(stacks[i_from][-num:])
    stacks[i_from] = stacks[i_from][:-num]
    
##    print(line)
##    for a in stacks:
##        print(a,stacks[a])

for a in stacks:
    print(a,stacks[a][-1])






