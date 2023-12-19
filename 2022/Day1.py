import numpy as np

f = open("./Input.dat")

elves = [0]
i=0

for line in f:
    if line=="\n":
        elves.append(0)
        i=i+1
    else:
        elves[i] += int(line)

elves = np.array(elves)
print(elves.max())

elf_sort = np.sort(elves)
print(elf_sort)

print(np.sum(elf_sort[-3:]))
