import numpy as np

f = open("./Day2 Input.dat")

   

tot = 0

for line in f:
    them = line[0]
    me = line[2]

    # They chose rock
    if them=='A':
        if me=='X':
            tot += 3; tot += 0
        elif me=='Y':
            tot += 1; tot += 3
        elif me=='Z':
            tot += 2; tot += 6

    # They chose paper
    elif them=='B':
        if me=='X':
            tot += 1; tot += 0
        elif me=='Y':
            tot += 2; tot += 3
        elif me=='Z':
            tot += 3; tot += 6
            
    elif them=='C':
        if me=='X':
            tot += 2; tot += 0
        elif me=='Y':
            tot += 3; tot += 3
        elif me=='Z':
            tot += 1; tot += 6
print(tot)
