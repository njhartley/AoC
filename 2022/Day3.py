import numpy as np

f = open("./Day3 Input.dat")

tot = 0

lines = f.readlines()
n_lines = len(lines)

for i in range(int(n_lines/3.)):
    elf_1 = list(lines[3*i][:-1])
    elf_2 = list(lines[3*i+1][:-1])  
    elf_3 = list(lines[3*i+2][:-1])

    both = list(set(elf_1) & set(elf_2) & set(elf_3))

    val = ord(both[0])
    if val>90:
        val1 = val-96
    else:
        val1 = val-38
    tot += val1
print(tot)



##for line in f:
##    size = int(0.5*(len(line)-1))
##    com_a = list(line[:size])
##    com_b = list(line[size:-1])
##    
##    both = list(set(com_a) & set(com_b))
##
##    val = ord(both[0])
##    if val>90:
##        val1 = val-96
##    else:
##        val1 = val+26-64
##
##print(tot)



