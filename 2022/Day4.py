import numpy as np
import re

f = open("./Day4 Input.dat")

tot = 0

#lines = f.readlines()
#n_lines = len(lines)

for line in f:
    num = re.split('-|,',line[:-1])
    elf1 = set(range(int(num[0]),1+int(num[1])))
    elf2 = set(range(int(num[2]),1+int(num[3])))

    n_overlap = len(elf1 & elf2)
    #print(line, len(elf1), len(elf2), n_overlap)
    
##    if len(elf1)==n_overlap or len(elf2)==n_overlap:
##        tot += 1
    if n_overlap>0:
        tot += 1
print(tot)
