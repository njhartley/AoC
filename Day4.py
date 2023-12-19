import numpy as np
from typing import List, Tuple

# Open the file and read the lines into a list
lines: List[str] = open("./Input/Day4.txt").read().splitlines()

n_line = np.ones(len(lines))

run_tot = 0
for j,line in enumerate(lines):
    idno,data = line.split(':')
    idno = idno.split()[1]
    num_in,num_out = data.split('|')
    num_in= num_in.split()
    num_out = num_out.split()

    i=0
    for num in num_in:
        i+=num_out.count(num)
    if i>0:
        idx_max = np.min((j+i+1,len(lines)))
        n_line[j+1:idx_max]+=n_line[j]
print(np.sum(n_line))



##run_tot = 0
##for line in f:
##    #print(line)
##    idno,data = line.split(':')
##    idno = idno.split()[1]
##    num_in,num_out = data.split('|')
##    num_in= num_in.split()
##    num_out = num_out.split()
##
##    #print(num_in)
##
##    i=0
##    for num in num_in:
##        i+=num_out.count(num)
##    if i>0:
##        run_tot += 2**(i-1)
##print(run_tot)
    
    
    
