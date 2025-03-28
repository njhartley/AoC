import numpy as np
from typing import List, Tuple

# Open the file and read the lines into a list
lines: List[str] = open("./Input/Day6.txt").read().splitlines()

# Open file as iterable
f = open("./Input/Day6.txt")

## Part 1
##times = np.array(f.readline().split()[1:],dtype=int)
##dists = np.array(f.readline().split()[1:],dtype=int)
##f.close()
##
###print(times)
###print(dists)
##
##run_prod = 1
##
##for (time,dist) in zip(times,dists):
##    ts = np.arange(0,time,1)
##    ds = ts * (time-ts)
##    tcount = np.sum(ds>dist)
##    
##    run_prod *= tcount
##print(run_prod)


time_f = int(f.readline().replace(" ","").split(':')[1])
dist_f = int(f.readline().replace(" ","").split(':')[1])

time=0; dist=0;
while dist<dist_f:
    time += 1
    dist = time * (time_f - time)
A1 = time

time=time_f; dist=0;
while dist<dist_f:
    time -= 1
    dist = time * (time_f - time)
A2 = time

print(A1,A2,1+A2-A1)

