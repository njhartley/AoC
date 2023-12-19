import numpy as np
from typing import List, Tuple

# Open the file and read the lines into a list
f = open("./Input/Day5.txt")

funcs = [[]]

seeds = f.readline().split()[1:]
f.readline()
f.readline()

## Get function information
n_func = 0
for line in f:
    if line=='\n':
        f.readline() # Skips map name
    try:
        n1,n2,n3 = line.split()
        ns = [int(i) for i in line.split()]
        funcs[n_func] = funcs[n_func] + ns
    except:
        #print("New function")
        n_func += 1
        funcs = funcs + [[]]
#print(funcs)

##locs = np.zeros(len(seeds)) ## Store location info
## For each seed, calculate location
##for i,seed in enumerate(seeds):
##    seed =int(seed)
##    #print("Seed number %d"%seed)
##    for dat in funcs:
##        arr = np.reshape(np.array(dat),(3,-1),order='F')
##        dest,sour,nval = arr[0],arr[1],arr[2]
##        #print(arr)
##
##        comp = (seed>=sour)*(seed<(sour+nval)) 
##        if comp.any():
##            idx = comp.nonzero()[0][0]
##            seed = dest[idx] + (seed - sour[idx])
##        else:
##            seed = seed
##    #print("Destination value %d"%seed)
##    locs[i] = seed
##
##print(seeds)
##print(locs)
##print(np.min(locs))


## Part 2

## Definitions of seed arrays
seed0 = np.array(seeds[::2],dtype=float)
seed1 = np.array(seeds[1::2],dtype=float)
tseed = seed0+seed1


## For each location, find valid seed
loc = 72260000
while loc:
    #print("Seed number %d"%seed)
    seed = loc
    for dat in funcs[::-1]:
        arr = np.reshape(np.array(dat),(3,-1),order='F')
        dest,sour,nval = arr[0],arr[1],arr[2]

        comp1 = (seed>=dest)
        comp2 = (seed<(dest+nval))
        comp = comp1*comp2
        #print(comp)
        if comp.any():
            idx = comp.nonzero()[0][0]
            seed = sour[idx] + (seed - dest[idx])
        else:
            seed = seed
        #print(seed)
    #print("Loc %d becomes seed %d"%(loc,seed))
    #print(loc,seed)
    ## Check if seed is in input
    comp = (seed>=seed0)*(seed<(tseed))
    if comp.any():
        print(loc,seed)
        break
    if loc>1e9:
        break
    loc = loc+1





            
            

    
    
