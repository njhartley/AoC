import numpy as np
from typing import List, Tuple

# Open the file and read the lines into a list
#lines: List[str] = open("./Input/Day13_test.txt").read().splitlines()

# Open file as iterable
f = open("./Input/Day13.txt")

arr_lst = [[]]
i=0

for line in f:
    if line=='\n':
        arr_lst.append([])
        i+=1
    else:
        arr_lst[i].append(list(line.strip().replace('.','0').replace('#','1')))

run_tot = 0           
for j,arr in enumerate(arr_lst):
    arr = np.array(arr,dtype=int)

    x,y = arr.shape

    for ix in np.arange(1,x,1):
        size = min(ix,x-ix)
        
        dx1 = arr[ix-size:ix+size]
        dx2 = np.flip(arr[ix-size:ix+size],axis=0)

        dx = np.abs(dx1 - dx2)

        if np.sum(dx)==2:
            run_tot += 100*ix
            #print("Box %d, horizontal symmetry at line %d"%(j,ix))

    for iy in np.arange(1,y,1):
        size = min(iy,y-iy)
        
        dy1 = arr[:,iy-size:iy+size]
        dy2 = np.flip(arr[:,iy-size:iy+size],axis=1)

        dy = np.abs(dy1 - dy2)

        if np.sum(dy)==2:
            run_tot += iy
            #print("Box %d, vertical symmetry at line %d"%(j,iy))
print(run_tot)

        
    
