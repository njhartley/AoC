import numpy as np
from typing import List, Tuple

# Open the file and read the lines into a list
lines: List[str] = open("./Input/Day11.txt").read().splitlines()

# Open file as iterable
#f = open("./Input/Day5.txt")

size1 = len(lines)
size2 = len(lines[0])

## Larger to hold expansion
arr = np.zeros((size1,size2))

## Place galaxies in original locations
ngal = 1
for i in range(size1):
    for j in range(size2):
        if lines[i][j]=='#':
            arr[i][j]=ngal
            ngal+=1
print("%d total galaxies"%(ngal-1))

## Expand horizontally
i=0
while i<size1:
    if np.max(arr[:,i])==0:
        arr[:,i]=-1
    i+=1
##        arr[:,i+1:] = arr[:,i:-1]
##        i+=2
##    else:
##        i+=1
## Expand vertically       
i=0
while i<size1:
    if np.max(arr[i,:])==0:
        arr[i,:]=-1
    i+=1
##        arr[i+1:,:] = arr[i:-1,:]
##        i+=2
##    else:
##        i+=1
#print(arr)


run_tot = 0
for i0 in np.arange(1,ngal):
    for j0 in np.arange(i0,ngal,1):
        #print(i0,j0)
        y0,x0 = np.where(arr==i0)
        y1,x1  = np.where(arr==j0)
        x0=x0[0]; x1=x1[0];
        y0=y0[0]; y1=y1[0]
        if x1<x0:
            x=x1; x1=x0; x0=x
        if y1<y0:
            y=y1; y1=y0; y0=y

        dx = arr[y0,x0:x1]
        dy = arr[y0:y1,x0]

        #print(i0,j0,np.sum(dx<0),np.sum(dy<0))
        
        dx = x1-x0 + (1e6-1)*(np.sum(dx<0))
        dy = y1-y0 + (1e6-1)*(np.sum(dy<0))
        #print(i0,j0,dx,dy,dx+dy)
        path = dx+dy
        run_tot += path
        

print(run_tot)



##run_tot = 0
##for i0 in np.arange(1,ngal):
##    for j0 in np.arange(i0,ngal,1):
##        #print(i0,j0)
##        coordi = np.where(arr==i0)
##        coordj = np.where(arr==j0)
##        dx = np.abs(coordi[0]-coordj[0])
##        dy = np.abs(coordi[1]-coordj[1])
##        #print(i0,j0,dx,dy,dx+dy)
##        path = dx+dy
##        run_tot += path[0]
##
##print(run_tot)
        

    
