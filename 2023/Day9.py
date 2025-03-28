import numpy as np
from typing import List, Tuple
from math import comb

# Open the file and read the lines into a list
lines: List[str] = open("./Input/Day9.txt").read().splitlines()

# Open file as iterable
#f = open("./Input/Day5.txt")

run_tot = 0
total_sum = 0

for line in lines:
    
    vals = np.array(line.split(),dtype=int)#[::-1]
    dvals = vals[1:]-vals[:-1]
    run_count = vals[-1]
    
    while np.max(np.abs(dvals))>0:        
        vals = dvals
        dvals = vals[1:]-vals[:-1]
        run_count += vals[-1]
    run_tot += run_count  
    
print(run_tot)

