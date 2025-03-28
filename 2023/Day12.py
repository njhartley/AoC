import numpy as np
from typing import List, Tuple
from itertools import combinations
import math

# Open the file and read the lines into a list
lines: List[str] = open("./Input/Day12.txt").read().splitlines()
n_line = len(lines)


def hash_count(string):
    sets = string.replace('.',' ').split()
    return np.array([len(i) for i in sets])

run_tot = 0    
for j,line in enumerate(lines):
    line_tot = 0
    
    dat_1,num_1 = line.split()

    dat = '?'.join(dat_1*5)
    num = 5*eval(num_1)

    nsq = len(dat)          # Length of line
    nums = np.array(num.split(','),dtype=int) # Final result - sets of hashes    
    sets = hash_count(dat) # Initial result - sets of non-gaps

    if sets[0]<nums[0]:
        dat = ''.join(['.']*sets[0]) + dat[sets[0]:]
    if sets[-1]<nums[-1]:
        dat = dat[:-sets[-1]] + ''.join(['.']*sets[-1])


    ## Get numbers of elements in string
    sprng_in = dat.count('#')
    quest = dat.count('?')
    sprng_tot = np.sum(nums)

    ## Get number of elements to be replaced
    n_sprng = sprng_tot-sprng_in
    n_gaps = quest-n_sprng

    print(n_sprng,n_gaps)
    print(math.factorial(quest))
    print(math.factorial(quest)/(math.factorial(n_sprng)*math.factorial(n_gaps)))

    ## Possible hash locations
    fill = list(combinations(range(quest),n_sprng))
   
    for comb in fill:
        dat_rep = dat
        #print(dat_rep)
        i=0
        while dat_rep.count('?'):
            if i in comb:
                dat_rep = dat_rep.replace('?','#',1)
            else:
                dat_rep = dat_rep.replace('?','.',1)
            i += 1
        if np.all(hash_count(dat_rep)==nums):
            line_tot += 1
                
    print("Line %d/%d, %d combinations"%((j+1),n_line,line_tot))
    run_tot += line_tot
    break
##print(run_tot)



## Part 1
##run_tot = 0    
##for j,line in enumerate(lines):
##    line_tot = 0
##    
##    dat,num = line.split()
##    print(dat)
##    nsq = len(dat)          # Length of line
##    nums = np.array(num.split(','),dtype=int) # Final result - sets of hashes    
##    sets = hash_count(dat) # Initial result - sets of non-gaps
##
##    if sets[0]<nums[0]:
##        dat = ''.join(['.']*sets[0]) + dat[sets[0]:]
##    if sets[-1]<nums[-1]:
##        dat = dat[:-sets[-1]] + ''.join(['.']*sets[-1])
##
##
##    ## Get numbers of elements in string
##    sprng_in = dat.count('#')
##    quest = dat.count('?')
##    sprng_tot = np.sum(nums)
##
##    ## Get number of elements to be replaced
##    n_sprng = sprng_tot-sprng_in
##    n_gaps = quest-n_sprng
##
####    print(n_sprng,n_gaps)
####    print(math.factorial(quest))
####    print(math.factorial(quest)/(math.factorial(n_sprng)*math.factorial(n_gaps)))
##
##    ## Possible hash locations
##    fill = list(combinations(range(quest),n_sprng))
##   
##    for comb in fill:
##        dat_rep = dat
##        #print(dat_rep)
##        i=0
##        while dat_rep.count('?'):
##            if i in comb:
##                dat_rep = dat_rep.replace('?','#',1)
##            else:
##                dat_rep = dat_rep.replace('?','.',1)
##            i += 1
##        if np.all(hash_count(dat_rep)==nums):
##            line_tot += 1
##                
##    print("Line %d/%d, %d combinations"%((j+1),n_line,line_tot))
##    run_tot += line_tot
##print(run_tot)  


    

    
    
