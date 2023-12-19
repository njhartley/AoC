import numpy as np
import re

f = open("./Day8 Input.dat")

grid = np.zeros((99,99))

## Generate grid as array
for i,line in enumerate(f):
    for j in range(99):
        grid[i][j]=line[j]

##tot = 0
##for i in range(1,98):
##    for j in range(1,98):     
##        val = grid[i][j]
##        left = val>grid[i,:j].max()
##        right= val>grid[i,j+1:].max()
##        top  = val>grid[:i,j].max()
##        bot  = val>grid[i+1:,j].max()
##        if any((left,right,top,bot)):
##            tot += 1
##print(tot + 4*98)

scenic_scores = np.zeros((99,99))

for i in range(99):
    for j in range(99):
        val = grid[i][j]
        #try:
        
        try:
            left = j - np.where(grid[i,:j]>=val)[0][-1]
        except:
            left = j    
        
        
        try:
            right= 1 + np.where(grid[i,j+1:]>=val)[0][0]
        except:
            right= 98-j
        
        
        try:
            top =  i - np.where(grid[:i,j]>=val)[0][-1]
        except:
            top = i
        
        try:
            bot =  1 + np.where(grid[i+1:,j]>=val)[0][0]
        except:
            bot = 98-i
            

        
        score = left*right*top*bot
        scenic_scores[i][j]=score
        if score>1e5:
            print(i,j,val,score)
            print(left)
            print(right)
            print(top)
            print(bot)

print(np.max(scenic_scores))

        
    
