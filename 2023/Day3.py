import numpy as np
import string
import re

f = open("./Input/Day3_test2.txt")

## Loop over array and label asterisks, get index of their positions
size=10
astks = np.zeros((size,size),dtype=object) ## Hold asterisk labels
ilab=0
symbs = []

#labels = list(string.ascii_lowercase)

for i,line in enumerate(f):
    #size= len(line.strip())
    for j,char in enumerate(list(line.strip())):
        if char=='*':
            astks[i,j]=('a'+str(ilab))
            ilab+=1
            symbs.append((i,j))
#print(astks)
#print(symbs)

## Label positions by which asterisk they are near
dist_bool = np.zeros((size,size),dtype=object)

for i in range(size):
    for j in range(size):
        val = np.array((i,j))
        sep = symbs-val
        #nrst = np.argmin(np.linalg.norm(sep,axis=1))
        #dist = np.min(np.linalg.norm(sep,axis=1))
        dists = np.floor(np.linalg.norm(sep,axis=1)/1.5)
        ast_indxs = np.where(dists==0)[0]

        if len(ast_indxs!=0):
            string = ''
            for idx in ast_indxs:
                string = string + 'a' + str(idx) + ','
            dist_bool[i][j]  = string
            
## Reads 1 for positions near to asterisks, 0 elsewhere
#print(dist_bool)

## Restart file
f.seek(0)

gear_nums = []
gear_labels = []

for i,line in enumerate(f):
    chars = list(line.strip())
    j=0
    while j<size:
        char = chars[j]
        dist = dist_bool[i][j]

        #print(j,char,dist)
        
        num = []; idx = []
        while char.isdigit():
            num.append(char)
            idx.append(dist)
            j += 1
            try:
                char=chars[j]
                dist=dist_bool[i][j]
            except:
                break
        if len(num)>0:
            s = int(''.join(num))
            idx = np.array(idx,dtype=str)
            #print(s)
            print(idx)

            #print(np.array(idx,dtype=str))
            #print(np.any(np.array(idx,dtype=str)!='0'))
            if np.any(idx!='0'):
                gear_nums.append(s)
                gear_labels.append(idx)
        j+=1


##for ii in range(len(gear_labels)):
##    arr = gear_labels[ii]
##    arr = np.delete(arr,np.where(arr=='0'))
##    print(arr)






### Part 1
## Loop over array and get indices of symbols
##symbs = []
##for i,line in enumerate(f):
##    size= len(line.strip())
##    for j,char in enumerate(list(line.strip())):
##        if char not in '.' and not char.isdigit():
##            symbs.append((i,j))
##symbs = np.array(symbs)
##
##
##dists = np.zeros((size,size))
##for i in range(size):
##    for j in range(size):
##        val = np.array((i,j))
##        sep = symbs-val
##        dist = np.min(np.linalg.norm(sep,axis=1))
##        if dist<1.5:
##            dists[i][j]=1
##        else:
##            dists[i][j]=0
#### Reads 1 for positions near to symbols, 0 elsewhere
###print(dists)
##
#### Restart file
##f.seek(0)
##
##part_nums = []
##
##for i,line in enumerate(f):
##    chars = list(line.strip())
##    j=0
##    while j<size:
##        char = chars[j]
##        dist = dists[i][j]
##
##        #print(j,char,dist)
##        
##        num = []; idx = []
##        while char.isdigit():
##            num.append(char)
##            idx.append(dist)
##            j += 1
##            try:
##                char=chars[j]
##                dist = dists[i][j]
##            except:
##                break
##        if len(num)>0:
##            s = int(''.join(num))
##            #print(s)
##            if np.max(np.array(idx))==1:
##                part_nums.append(s)
##        j+=1
##print(np.sum(np.array(part_nums)))            

            
